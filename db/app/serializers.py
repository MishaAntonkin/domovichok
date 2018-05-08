from flask import request

from .models import *
from . import db
from .validation import *


class HousesFilterSerializar():
    needed_params = ['price_gte', 'price_lte', 'district', 'currency', 'area']
    model = Flat

    def __init__(self, filter_dict):
        self.unfilters = filter_dict

    def __call__(self, *args, **kwargs):
        query_filter = []
        for param in self.needed_params:
            cur_param = self.unfilters.get(param)
            if cur_param == None or cur_param == '':
                continue
            if param == 'price_gte':
                query_filter.append(Flat.price > cur_param)
            elif param == 'price_lte':
                query_filter.append(Flat.price < cur_param)
            elif param == 'district':
                query_filter.append(Flat.district == cur_param)
            elif param == 'currency':
                query_filter.append(Flat.currency == cur_param)
            elif param == 'area':
                query_filter.append(Flat.area == cur_param)
        print(query_filter)
        return self.model.query.filter(*query_filter)


class SaveHousesSerializer():
    model = Flat

    def __init__(self, data):
        self.data = data
        self.flat = None
        if self.validate():
            self.clean_data()
            self.create_or_update()

    def validate(self):
        obj_keys = {i for i in dir(self.model) if not i.startswith('__')}
        data_keys = set(self.data.keys())
        if data_keys.issubset(obj_keys):
            return True
        else:
            raise Exception
        pass

    def clean_data(self):
        """
        not best solution but temporary
        """
        data = {}
        for key, val in self.data.items():
            if key == 'area':
                data[key] = float(val)
            elif key == 'price':
                data[key] = float(val)
            else:
                data[key] = val
        self.data = data

    def create_or_update(self):
        exist_flat = Flat.query.filter_by(url=self.data['url']).first()
        if exist_flat is not None:
            print('On create update')
            exist_flat.update(self.data)
        else:
            print('On create create')
            exist_flat = Flat(**self.data)
            db.session.add(exist_flat)
        self.flat = exist_flat

    def __call__(self, *args, **kwargs):
        return self.flat


