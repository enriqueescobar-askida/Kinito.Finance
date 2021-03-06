from Common.StockType.Funds.ExchangeTraded.ExchangeTradedFund import ExchangeTradedFund


class Ftse(ExchangeTradedFund):
    ShortName: str
    LongName: str
    Ticker: str
    CapType: str
    Size: int

    def __init__(self):
        self.LongName = 'Financial Times StockType Exchange 100 Index'
        self.ShortName = 'FTSE'
        self.Ticker = '^FTSE'
        self.CapType = 'L'
        self.Size = 100
