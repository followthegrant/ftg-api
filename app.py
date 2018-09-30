from flask import Flask, request, jsonify

from elastic import search

import settings


app = Flask(__name__)


@app.route("/")
def index():
    q = request.args.get('q')
    data = search(q)
    response = jsonify(data)
    if settings.ALLOW_ALL:
        response.headers.add('Access-Control-Allow-Origin', '*')
    return response
