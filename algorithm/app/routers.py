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
        return jsonify(h_external), 200
    try:
        houses = main(h_external, data['cri'])
    except:
        print('Something went wrong')
    #print(houses)
    #houses_w= []
    #for house in houses:
    #    houses_w.append(house.data)
    #print(houses_w)
    #return_data = json.dumps(houses_w)
    return 'yes' #return_data


def check_ip(ip_addr):
    return True if ip_addr in app.config['WHITE_LIST'] else False
