import yfinance as yf
from enum import Enum


class SpecificInfo(Enum):
    OPEN = 'Open'
    CLOSE = 'Close'
    LOW = 'Low'
    HIGH = 'High'
    ADJ_CLOSE = 'Adj Close'
    VOLUME = 'Volume'


def stock_info(ticker, start, end, only=None):
    """
    Function that brings us information about the prices and volume traded of a stock
    :param ticker: Stock symbol. Example -> Visa-ticker=V, 3M-company-ticker=MMM
    :param start: Starting date of desire data
    :param end: Ending date of desire data
    :param only: If we only want a specific data
    :return: Dictionary with info
    """

    if only is None:
        df_yahoo = yf.download(ticker, start=start, end=end, progress=False).to_dict()
        dict_stock_info = {info_stock: {str(date.to_pydatetime().date()): value for date, value in dict_info.items()}
                           for info_stock, dict_info in df_yahoo.items()}
        return dict_stock_info

    elif only.title() in [x.value for x in SpecificInfo]:
        df_yahoo = yf.download(ticker, start=start, end=end, progress=False).to_dict()
        dict_stock_info = {info_stock: {str(date.to_pydatetime().date()): value for date, value in dict_info.items()}
                           for info_stock, dict_info in df_yahoo.items()}
        return {only.title(): dict_stock_info[only.title()]}

    else:
        return {"message": "Specific information key is invalid. Only 'Open', 'Close', 'High', "
                           "'Low', 'Adj Close' and 'Volume' are accepted!"}
