from flask import Flask, request
from flask_restful import Resource, Api
from stock_info import stock_info
from today import today

app = Flask(__name__)
api = Api(app)


class StockAllInfo(Resource):
    def get(self, name):
        data_request = request.get_json()
        dict_info = stock_info(name, data_request['start'], data_request['end'])
        return dict_info, 200 if dict_info['Open'] else 404


class OpenPriceShare(Resource):
    def get(self, name):
        data_request = request.get_json()
        dict_info = stock_info(name, data_request['start'], data_request['end'], only='open')
        return dict_info, 200 if dict_info['Open'] else 404


class ClosePriceShare(Resource):
    def get(self, name):
        data_request = request.get_json()
        dict_info = stock_info(name, data_request['start'], data_request['end'], only='close')
        return dict_info, 200 if dict_info['Close'] else 404


class LowPriceShare(Resource):
    def get(self, name):
        data_request = request.get_json()
        dict_info = stock_info(name, data_request['start'], data_request['end'], only='low')
        return dict_info, 200 if dict_info['Low'] else 404


class HighPriceShare(Resource):
    def get(self, name):
        data_request = request.get_json()
        dict_info = stock_info(name, data_request['start'], data_request['end'], only='high')
        return dict_info, 200 if dict_info['High'] else 404


class AdjClosePriceShare(Resource):
    def get(self, name):
        data_request = request.get_json()
        dict_info = stock_info(name, data_request['start'], data_request['end'], only='adj close')
        return dict_info, 200 if dict_info['Adj Close'] else 404


class VolumeShare(Resource):
    def get(self, name):
        data_request = request.get_json()
        dict_info = stock_info(name, data_request['start'], data_request['end'], only='volume')
        return dict_info, 200 if dict_info['Volume'] else 404


api.add_resource(StockAllInfo, '/<string:name>')
api.add_resource(OpenPriceShare, '/<string:name>/open')
api.add_resource(OpenPriceShare, '/<string:name>/close')
api.add_resource(OpenPriceShare, '/<string:name>/low')
api.add_resource(OpenPriceShare, '/<string:name>/high')
api.add_resource(OpenPriceShare, '/<string:name>/adj-close')
api.add_resource(OpenPriceShare, '/<string:name>/volume')


app.run(port=6787)

# @app.route('/<string:name>/today')
# def today_price(name):
#     return jsonify(today(name))



