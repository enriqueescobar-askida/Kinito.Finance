import pandas as pd
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class RsiIndicator(AbstractTechIndicator):
    __avgGain: pd.core.series.Series
    __avgLoss: pd.core.series.Series
    __delta: pd.core.series.Series
    __period: int
    __rs: pd.core.series.Series
    _rsi: pd.core.series.Series

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._Label = 'RSI'
        self.__delta = y_stock_option.HistoricalData[self._col].diff(1)
        self.__setPeriod(14)
        self.__setUp()
        self.__setDown()
        self.__setRsi()

    def __setUp(self):
        up = self.__delta.copy()
        up[up < 0] = 0
        self.__setAvgGain(up)

    def __setDown(self):
        down = self.__delta.copy()
        down[down > 0] = 0
        self.__setAvgLoss(down)

    def __setPeriod(self, a_int: int):
        self.__period = a_int

    def __setAvgGain(self, up: pd.core.series.Series):
        self.__avgGain = up.rolling(window=self.__period).mean()

    def __setAvgLoss(self, down: pd.core.series.Series):
        self.__avgLoss = abs(down.rolling(window=self.__period).mean())

    def __setRsi(self):
        self.__rs = self.__avgGain / self.__avgLoss
        self._rsi = 100.0 - (100.0 / (1.0 + self.__rs))
