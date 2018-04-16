import json

from flask import Flask, request

from mainalg import main

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.data)
    data = json.loads(request.data)
    print(data)
    print(type(data))
    houses = main(data['houses'], data['cri'])
    print(houses)
    houses_w= []
    for house in houses:
        houses_w.append(house.data)
    print(houses_w)
    return_data = json.dumps(houses_w)
    return return_data

if __name__ == "__main__":
    app.run(debug=True, port=5000)