from flask import Flask, request, jsonify

from elastic import search


app = Flask(__name__)


@app.route("/")
def index():
    q = request.args.get('q')
    data = search(q)
    return jsonify(data)
