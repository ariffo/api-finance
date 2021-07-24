from flask import Flask, request
from flask_restful import Resource, Api
from stock_info import stock_info
from today import today
from valid_specific_info import valid_specific_info
from stocks_available import ticker_valido

app = Flask(__name__)
api = Api(app)


class StockAllInfo(Resource):
    def get(self, name):
        data_request = request.get_json()
        dict_info = stock_info(name, data_request['start'], data_request['end'])
        return dict_info, 200 if dict_info['Open'] else 404


class StockSpecificInfo(Resource):
    def get(self, name, info):
        data_request = request.get_json()
        dict_info = stock_info(name, data_request['start'], data_request['end'], only=info)
        info_valid_and_data_exists = (valid_specific_info(info) and
                                     next(filter(lambda x: bool(dict_info[x]) is True, dict_info), None))
        return dict_info, 200 if info_valid_and_data_exists else 404


class StockTodayPrice(Resource):
    def get(self, name):
        return today(name), 200 if ticker_valido(name) else 404


api.add_resource(StockAllInfo, '/<string:name>')
api.add_resource(StockSpecificInfo, '/<string:name>/<string:info>')
api.add_resource(StockTodayPrice, '/<string:name>/today')


if __name__ == '__main__':

    app.run(port=6787)
