import json

from flask import Flask, request
import requests

from mainalg import main

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.data)
    data = json.loads(request.data)
    print(data)
    print(type(data))
    r = requests.get('http://127.0.0.1:8001/houses/filter', params=data['filters'])
    if r.status_code == 200:
        h_external = r.json()
        print(h_external)
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

if __name__ == "__main__":
    app.run(debug=True, port=8003)