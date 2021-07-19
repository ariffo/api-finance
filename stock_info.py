import pandas as pd
import yfinance as yf

start = '2000-01-01'
end = '2000-01-20'

df_yahoo = yf.download('AAPL', start=start, end=end, progress=False).to_dict()

print(df_yahoo)
print(type(df_yahoo))

# def stock_info(ticker, start, end, only=False):
