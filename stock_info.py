import yfinance as yf

start = '2000-01-01'
end = '2000-01-05'

df_yahoo = yf.download('AAPL', start=start, end=end, progress=False).to_dict()
dict_stock_info = {stock_info: {str(date.to_pydatetime().date()): value for date, value in dict_info.items()}
                   for stock_info, dict_info in df_yahoo.items()}

print(df_yahoo)
print(type(df_yahoo))

print("------------")
print(dict_stock_info)

# def stock_info(ticker, start, end, only=False):

# .to_pydatetime()
