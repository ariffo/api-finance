import yfinance as yf
from stocks_available import ticker_valido


def today(ticker):
    """
    Function that brings up the current price of Dow Jones shares
    :param ticker: Stock symbol. Example -> Visa-ticker=V, 3M-company-ticker=MMM
    :return: A dictionary with current price (Close price in yfinance terms)
    """

    if ticker_valido(ticker):
        currently_price = yf.Ticker(ticker).history(period='1d')['Close'][0]
        return {'Currently Price': currently_price}

    else:
        return {'message': 'Error, ticker no valid. Only available Dow Jones tickers'}
