from enum import Enum


class Shares(Enum):
    MMM = '3M CO.'
    AXP = 'American Express CO.'
    AMGN = 'Amgen INC.'
    AAPL = 'Apple INC.'
    BA = 'Boeing CO.'
    CAT = 'Caterpillar INC.'
    CVX = 'Chevron CORP.'
    CSCO = 'Cisco INC.'
    KO = 'Coca-Cola CO.'
    DOW = 'Dow INC.'
    GS = 'Goldman Sachs'
    HD = 'The Home Depot INC.'
    HON = 'Honeywell'
    IBM = 'IBM CORP.'
    INTC = 'Intel CORP.'
    JNJ = 'Johnson & Johnson'
    JPM = 'JPMorgan Chase & CO.'
    MCD = "McDonald's CORP."
    MRK = 'Merck CO.'
    MSFT = 'Microsoft CORP.'
    NKE = 'Nike INC.'
    PG = 'Procter & Gamble CO.'
    CRM = 'Salesforce'
    TRV = 'Travelers INC.'
    UNH = 'United Health INC.'
    VZ = 'Verizon INC.'
    V = 'Visa INC.'
    WBA = 'Walgreens Boots Alliance INC.'
    WMT = 'Walmart'
    DIS = 'Walt Disney'


def ticker_valido(ticker):
    """
    Function that tells us if the stock belongs to the Dow Jones
    :param ticker: Stock symbol. Example -> Visa-ticker=V, 3M-company-ticker=MMM
    :return: True if stock belongs to the Down Jones, False if not.
    """

    if ticker.upper() in [share.name for share in Shares]:
        return True

    else:
        return False
