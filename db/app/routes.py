from flask import json, request, jsonify

from app import app, db
from .models import Flat


@app.route('/', methods=['GET'])
def main():
    return 'main'


@app.route('/houses/', methods=['GET'])
def get_houses():
    flats = Flat.query.all()
    return_list = []
    for fl in  flats:
        return_list.append(fl.row2dict())
    return jsonify(return_list), 200


@app.route('/houses/<int:id>/', methods=['GET'])
def get_house(id):
    try:
        flats = Flat.query.get(id)
    except:
        return jsonify({'result': 'error', 'message': 'db error'}), 403
    if flats is None:
        return jsonify({'result': 'error', 'message': 'id does not exist'}), 403
    return jsonify(flats.row2dict()), 200


@app.route('/houses/', methods=['POST'])
def save_houses():
    data = request.json
    try:
        for flat in data:
            fl = Flat(district=flat['district'], name=flat['name'], price=flat['price'])
            db.session.add(fl)
    except:
        print("invalid data")
        return jsonify({'result': 'error'}), 403
    else:
        db.session.commit()
    return json.dumps({'result': 'ok'}), 201


@app.route('/houses/<int:id>', methods=['PUT'])
def update_houses():

    flat = Flat.query.get(id)
    if flat is None:
        return jsonify({'result': 'error', 'message': 'id does not exist'}), 403
    try:
        data = request.json
        flat.update(data)
    except:
        return jsonify({'result': 'error', 'message': 'invalid data to update'}), 403
    return json.dumps({'result': 'ok'})


@app.route('/houses/<int:id>/', methods=['DELETE'])
def delete_houses(id):
    try:
        flat = Flat.query.get(id)
        print(flat)
        db.session.delete(flat)
        db.session.commit()
    except:
        return jsonify({'result': 'error', 'message': 'id does not exist'}), 403
    id_delete = 'id - {} deleted'.format(id)
    return jsonify({'result': id_delete}), 202
