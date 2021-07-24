import yfinance as yf
from valid_specific_info import valid_specific_info, SpecificInfo


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
    elif valid_specific_info(only):
        df_yahoo = yf.download(ticker, start=start, end=end, progress=False).to_dict()
        dict_stock_info = {info_stock: {str(date.to_pydatetime().date()): value for date, value in dict_info.items()}
                           for info_stock, dict_info in df_yahoo.items()}
        return {only.title(): dict_stock_info[SpecificInfo[only.upper()].value]}
    else:
        return {"message": "Specific information key is invalid. Only 'open', 'close', 'high', "
                           "'low', 'adj_close' and 'volume' are accepted!"}
