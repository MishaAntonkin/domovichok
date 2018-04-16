import json

from flask import Flask, request

from parer import parse_data

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return_data = parse_data()
    parsed_json = json.dumps(return_data)
    response = app.response_class(
        response=parsed_json,
        status=200,
        mimetype='application/json'
    )
    print(json.loads(parsed_json))
    return response


if __name__ == '__main__':
    app.run(debug=True, port=8001)
