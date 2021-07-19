from flask import Flask, jsonify, request
import yfinance as yf

app = Flask(__name__)

start = '2000-01-01'
end = '2000-01-05'


@app.route('/<string:name>')
def all_info(name):
    data_request = request.get_json()
    return jsonify(yf.download('AAPL', start=start, end=end, progress=False).to_dict())


app.run(port=6787)