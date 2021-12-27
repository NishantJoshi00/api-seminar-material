from flask import Flask, request, jsonify
import shelve

app = Flask(__name__)

friends = {}

@app.route('/')
def index():
    return 'Don\'t look for anything, nothing\'s there.'


@app.route('/friends', methods=['GET'])
def list_friends():
    return jsonify({
        'count': len(friends),
        'friends': list(friends.items())
    })


@app.route('/friends/<int:id>')
def get_friend(id):
    id = str(id)
    if id in friends:
        return jsonify({
            'id': id,
            'name': friends[id],
        })
    else:
        return jsonify({
            'error': 'Not found',
            'message': 'Really!! I don\'t know who that is.',
        })


@app.route('/friends', methods=['POST'])
def add_friend():
    id = str(len(friends))
    friends[id] = dict(request.form).get('name')
    print(f"Added {friends[id]} with id {id}")
    return jsonify({
        'id': id,
        'name': friends[id],
    })



@app.route('/friends/<int:id>', methods=['PUT'])
def edit_friend(id):
    id = str(id)
    friends[id] = request.form['name']
    return jsonify({
        'id': id,
        'name': friends[id],
    })



if __name__ == "__main__":
    app.run()