from flask import request

from .models import *
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
            if cur_param == None:
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

        return self.model.query.filter(*query_filter)


class SaveHousesSerializer():
    model = Flat

    def __init__(self, data):
        self.data = data
        if self.validate():
            self.clean_data()

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
        not best solution but temporarry
        """
        data = {}
        for key, val in self.data.items():
            if key == 'area':
                data[key] = clean_area(val)
            elif key == 'price':
                data[key] = clean_price(val)
                data['currency'] = clean_currency(val)
            else:
                data[key] = val
        print(data)
        self.data = data

    def __call__(self, *args, **kwargs):
        return Flat(**self.data)


