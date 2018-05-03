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
    r = requests.get('{}/houses/filter/'.format(app.config['DB_ADDRESS']), params=data['filters'])
    if r.status_code == 200:
        h_external = r.json()
        print(h_external)
    try:
        houses = main(h_external['data'], data['cri'])
        print(houses)
        houses_w = []
        for house in houses:
           houses_w.append(house.data)
    except Exception as E:
        print(E)
        print('Something went wrong')
    else:
        print(houses_w)
        return jsonify(houses_w), 200
    #print(houses)
    #houses_w= []
    #for house in houses:
    #    houses_w.append(house.data)
    #print(houses_w)
    #return_data = json.dumps(houses_w)
    return jsonify('Error'), 400

def check_ip(ip_addr):
    return True if ip_addr in app.config['WHITE_LIST'] else False
