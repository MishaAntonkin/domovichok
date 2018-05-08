from flask import json, request, jsonify

from app import app, db
from .models import Flat
from .serializers import *


@app.route('/', methods=['GET'])
def main():
    return 'main'


@app.route('/houses/', methods=['GET'])
def get_houses():
    page = request.args.get('page', 1, type=int)
    flats = Flat.query.paginate(page, app.config['POSTS_PER_PAGE'], False)
    return_list = []
    for fl in flats.items:
        return_list.append(fl.row2dict())
    response = {
        'has_next': flats.has_next,
        'has_prev': flats.has_prev,
        'data': return_list
    }
    return jsonify(response), 200


@app.route('/houses/filter/', methods=['GET'])
def get_houses_filter():
    flats = HousesFilterSerializar(request.args)
    page = request.args.get('page', 1, type=int)
    flats = flats().paginate(page, app.config['POSTS_PER_PAGE'], False)
    flats_list = []
    for fl in flats.items:
        flats_list.append(fl.row2dict())
    response = {
        'has_next': flats.has_next,
        'has_prev': flats.has_prev,
        'data': flats_list
    }
    return jsonify(response), 200


@app.route('/houses/<int:pk>/', methods=['GET'])
def get_house(pk):
    try:
        flats = Flat.query.get(pk)
    except Exception as e:
        print(e)
        return jsonify({'result': 'error', 'message': 'db error'}), 403
    if flats is None:
        return jsonify({'result': 'error', 'message': 'id does not exist'}), 403
    return jsonify(flats.row2dict()), 200


@app.route('/houses/', methods=['POST'])
def save_houses():
    data = request.json
    print(data)
    try:
        for flat in data:
            fl = SaveHousesSerializer(flat)
    except Exception as e:
        print("invalid data - {}".format(e))
        return jsonify({'result': 'error'}), 403
    else:
        db.session.commit()
    return jsonify({'result': 'ok'}), 201


@app.route('/houses/<int:pk>/', methods=['PUT'])
def update_houses(pk):
    flat = Flat.query.get(pk)
    if flat is None:
        return jsonify({'result': 'error', 'message': 'id does not exist'}), 403
    try:
        data = request.json
        flat.update(data)
    except Exception as e:
        print(e)
        return jsonify({'result': 'error', 'message': 'invalid data to update'}), 403
    else:
        db.session.commit()
    return jsonify({'result': 'ok'}), 200


@app.route('/houses/<int:pk>/', methods=['DELETE'])
def delete_houses(pk):
    try:
        flat = Flat.query.get(pk)
        print(flat)
        db.session.delete(flat)
        db.session.commit()
    except:
        return jsonify({'result': 'error', 'message': 'id does not exist'}), 403
    id_delete = 'id - {} deleted'.format(pk)
    return jsonify({'result': id_delete}), 202

