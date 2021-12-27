from database import client
from flask import Flask, request, jsonify, redirect
from hashlib import md5
from urllib.parse import urlparse
app = Flask(__name__)

db = client.test


@app.route('/')
def index():
    return 'This is a ContactBook API. Nothing to see here.'

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    obj = {
        'name': name,
        'email': email,
        'phone': phone,
    }
    db.cts.insert_one(obj)
    return jsonify({
        'name': name,
        'email': email,
        'phone': phone,
    })

## Create a find route with args to find by name or email or phone
@app.route('/find', methods=['GET'])
def find():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    if name:
        obj = db.cts.find_one({'name': name})
        if obj:
            return jsonify({
                'name': obj['name'],
                'email': obj['email'],
                'phone': obj['phone'],
            })
        else:
            return jsonify({
                'error': 'Not found',
                'message': 'The contact you requested was not found.',
            })
    elif email:
        obj = db.cts.find_one({'email': email})
        if obj:
            return jsonify({
                'name': obj['name'],
                'email': obj['email'],
                'phone': obj['phone'],
            })
        else:
            return jsonify({
                'error': 'Not found',
                'message': 'The contact you requested was not found.',
            })
    elif phone:
        obj = db.cts.find_one({'phone': phone})
        if obj:
            return jsonify({
                'name': obj['name'],
                'email': obj['email'],
                'phone': obj['phone'],
            })
        else:
            return jsonify({
                'error': 'Not found',
                'message': 'The contact you requested was not found.',
            })
    else:
        return jsonify({
            'error': 'Not found',
            'message': 'The contact you requested was not found.',
        })

# Create a edit route with args to edit by name or email or phone
@app.route('/edit', methods=['PUT'])
def edit():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    if name:
        obj = db.cts.find_one({'name': name})
        if obj:
            obj['name'] = request.form.get('name') if request.form.get('name') else obj['name']
            obj['email'] = request.form.get('email') if request.form.get('email') else obj['email']
            obj['phone'] = request.form.get('phone') if request.form.get('phone') else obj['phone']
            db.cts.replace_one({'name': name}, obj)
            return jsonify({
                'name': obj['name'],
                'email': obj['email'],
                'phone': obj['phone'],
            })
        else:
            return jsonify({
                'error': 'Not found',
                'message': 'The contact you requested was not found.',
            })
    elif email:
        obj = db.cts.find_one({'email': email})
        if obj:
            obj['name'] = request.form.get('name') if request.form.get('name') else obj['name']
            obj['email'] = request.form.get('email') if request.form.get('email') else obj['email']
            obj['phone'] = request.form.get('phone') if request.form.get('phone') else obj['phone']
            db.cts.replace_one({'email': email}, obj)
            return jsonify({
                'name': obj['name'],
                'email': obj['email'],
                'phone': obj['phone'],
            })
        else:
            return jsonify({
                'error': 'Not found',
                'message': 'The contact you requested was not found.',
            })
    elif phone:
        obj = db.cts.find_one({'phone': phone})
        if obj:
            obj['name'] = request.form.get('name') if request.form.get('name') else obj['name']
            obj['email'] = request.form.get('email') if request.form.get('email') else obj['email']
            obj['phone'] = request.form.get('phone') if request.form.get('phone') else obj['phone']
            db.cts.replace_one({'phone': phone}, obj)
            return jsonify({
                'name': obj['name'],
                'email': obj['email'],
                'phone': obj['phone'],
            })



if __name__ == '__main__':
    app.run(debug=True)
    