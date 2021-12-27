from database import client
from flask import Flask, request, jsonify, redirect
from hashlib import md5
from urllib.parse import urlparse

app = Flask(__name__)

db = client.test


@app.route('/')
def index():
    return 'This is a shortener API. Nothing to see here.'


@app.route('/api/shorten', methods=['POST'])
def shorten():
    url = request.form.get('url')
    try:
        b = urlparse(url)
        
        if b.scheme == '':
            raise ValueError('Invalid URL')
    except Exception as e:
        print(e)
        return jsonify({
            'error': 'Invalid URL',
            'message': 'The URL you provided is invalid.',
        })
    obj = {
        'url': url,
        'hash': md5(url.encode('utf-8')).hexdigest(),
    }
    # This must contain the url_root and the hash
    generated_url = f"{request.url_root}{obj['hash']}"
    db.urls.insert_one(obj)
    return jsonify({
        'url': url,
        'shortened_url': generated_url,
    })
    

@app.route('/<hashs>')
def redirects(hashs):
    try:
        url = db.urls.find_one({'hash': hashs})
        print(hashs)
        print(url['url'])
        return redirect(url['url'], code=302)
    except Exception as e:
        print(e)
        return jsonify({
            'error': 'Not found',
            'message': 'The URL you requested was not found.',
        })


app.run(debug=True)