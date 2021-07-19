import yfinance as yf


def stock_info(ticker, start, end, only=None):
    if only is None:
        df_yahoo = yf.download(ticker, start=start, end=end, progress=False).to_dict()
        dict_stock_info = {stock_info: {str(date.to_pydatetime().date()): value for date, value in dict_info.items()}
                           for stock_info, dict_info in df_yahoo.items()}
        return dict_stock_info
    else:
        df_yahoo = yf.download(ticker, start=start, end=end, progress=False).to_dict()
        dict_stock_info = {info_stock: {str(date.to_pydatetime().date()): value for date, value in dict_info.items()}
                           for info_stock, dict_info in df_yahoo.items()}
        return {only: dict_stock_info[only]}


print(stock_info('AAPL', start='2000-01-01', end='2000-01-05', only='Open'))

