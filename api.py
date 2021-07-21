from flask import Flask, jsonify, request
from stock_info import stock_info

app = Flask(__name__)


@app.route('/<string:name>')
def all_info(name):
    data_request = request.get_json()
    dict_info = stock_info(name, data_request['start'], data_request['end'])
    return jsonify(dict_info)


@app.route('/<string:name>/open')
def open_price_info(name):
    data_request = request.get_json()
    dict_info = stock_info(name, data_request['start'], data_request['end'], only='open')
    return jsonify(dict_info)


@app.route('/<string:name>/close')
def close_price_info(name):
    data_request = request.get_json()
    dict_info = stock_info(name, data_request['start'], data_request['end'], only='close')
    return jsonify(dict_info)


@app.route('/<string:name>/high')
def high_price_info(name):
    data_request = request.get_json()
    dict_info = stock_info(name, data_request['start'], data_request['end'], only='high')
    return jsonify(dict_info)


@app.route('/<string:name>/low')
def low_price_info(name):
    data_request = request.get_json()
    dict_info = stock_info(name, data_request['start'], data_request['end'], only='low')
    return jsonify(dict_info)


@app.route('/<string:name>/adj-close')
def adj_close_price_info(name):
    data_request = request.get_json()
    dict_info = stock_info(name, data_request['start'], data_request['end'], only='adj close')
    return jsonify(dict_info)


@app.route('/<string:name>/volume')
def volume_stock_info(name):
    data_request = request.get_json()
    dict_info = stock_info(name, data_request['start'], data_request['end'], only='volume')
    return jsonify(dict_info)


app.run(port=6787)
