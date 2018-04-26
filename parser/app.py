import json

from flask import Flask, request
import requests

from parer import parse_data
from utils import chunk_generator
from config import Config, REST_DB_HOST

app = Flask(__name__)
app.config.from_object(Config)


def send_data():
    return_data = parse_data()
    print(return_data)
    chunks = chunk_generator(return_data, 20)
    for data in chunks:
        print(' - {}'.format(data))
        r = requests.post(REST_DB_HOST + '/houses/', json=data)
        if r.status_code != 201:
            #  write something in log
            print('error send data')
            break
    else:
        return True


@app.route('/', methods=['GET', 'POST'])
def index():
    return "success" if send_data() else 'error'


if __name__ == '__main__':
    app.run(debug=True, port=8002)
