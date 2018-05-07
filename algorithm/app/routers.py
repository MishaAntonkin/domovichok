import json

from flask import request, jsonify
import requests

from mainalg import main
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.remote_addr)
    print(request.data)
    if not check_ip(request.remote_addr):
        return 'error', 403
    if request.data:
        data = json.loads(request.data)
        print(data)
        print(type(data))
    else:
        data = {'filters': {'district': 'Dnipr'}}
    flats_to_alg = get_all_data(data['filters'])
    try:
        houses = main(flats_to_alg, data['cri'])
        print(houses)
        houses_w = []
        for house in houses:
           houses_w.append(house.data)
    except Exception as E:
        print(E)
        print('Something went wrong')
    else:
        houses_w.sort(key=lambda item: item['weight'], reverse=True)
        print(houses_w)
        return jsonify(houses_w), 200
    return jsonify('Error'), 400


def check_ip(ip_addr):
    return True if ip_addr in app.config['WHITE_LIST'] else False


def get_all_data(filters):
    if 'page' not in filters:
        filters['page'] = 1
    filtered_flats = []
    with requests.session() as session:
        has_next = True
        while has_next:
            r = session.get('{}/houses/filter/'.format(app.config['DB_ADDRESS']), params=filters)
            if r.status_code == 200:
                resp_data = r.json()
                filtered_flats.extend(resp_data['data'])
                has_next = resp_data['has_next']
                if has_next:
                    filters['page'] += 1
            else:
                print('Error from db in algorthm')
                has_next = False
    return filtered_flats
