import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from pandas import DataFrame
from Common.TechIndicators.AbstractTechIndicator import AbstractTechIndicator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption


class RsiIndicator(AbstractTechIndicator):
    _data: DataFrame = DataFrame()
    __period: int

    def __init__(self, y_stock_option: YahooStockOption):
        super().__init__(y_stock_option)
        self._name = 'RSI'
        self._label += self._name
        self._main_label += ' ' + self._label
        self.__setPeriod(14)
        self._setData(y_stock_option)

    def GetData(self) -> DataFrame:
        return self._data

    def PlotData(self) -> plt:
        plt.figure(figsize=self._fig_size)
        plt.style.use(self._plot_style)
        colors = cm.coolwarm
        for a_ind, col in enumerate(self._data.columns[-1:self._data.columns.size]):
            an_alpha: float = 0.5 if a_ind != 0 else 1.0
            self._data[col].plot(alpha=an_alpha)
            print('i', a_ind)
        plt.axhline(10, linestyle='--', label='10%', alpha=0.50, color='gray')
        plt.axhline(20, linestyle='--', label='20%', alpha=0.50, color='orange')
        plt.axhline(30, linestyle='--', label='30%', alpha=0.50, color='green')
        plt.axhline(40, linestyle='--', label='40%', alpha=0.50, color='red')
        plt.axhline(60, linestyle='--', label='60%', alpha=0.50, color='red')
        plt.axhline(70, linestyle='--', label='70%', alpha=0.50, color='green')
        plt.axhline(80, linestyle='--', label='80%', alpha=0.50, color='orange')
        plt.axhline(90, linestyle='--', label='90%', alpha=0.50, color='gray')
        plt.title(self._main_label)
        plt.xlabel(self._x_label)
        plt.xticks(rotation=self._x_ticks_angle)
        plt.ylabel(self._y_label)
        plt.legend(loc=self._legend_place)
        plt.grid(True)
        return plt

    def _setData(self, y_stock_option: YahooStockOption):
        self._data[self._col] = y_stock_option.DataFrame[self._col]
        delta: pd.core.series.Series = y_stock_option.DataFrame[self._col].diff(1)
        self._data['Delta'] = delta
        avgGain: pd.core.series.Series = self.__getAverageGain(delta)
        self._data['AverageGain'] = avgGain
        avgLoss: pd.core.series.Series = self.__getAverageLoss(delta)
        self._data['AverageLoss'] = avgLoss
        rs = avgGain / avgLoss
        self._data['RelativeStrength'] = rs
        self._data[self._name] = 100.0 - (100.0 / (1.0 + rs))
        self._low_high = (2, 3)

    def __setPeriod(self, a_int: int):
        self.__period = a_int

    def __getAverageGain(self, delta: pd.core.series.Series) -> pd.core.series.Series:
        up = delta.copy()
        up[up < 0] = 0
        return up.rolling(window=self.__period).mean()

    def __getAverageLoss(self, delta: pd.core.series.Series) -> pd.core.series.Series:
        down = delta.copy()
        down[down > 0] = 0
        return abs(down.rolling(window=self.__period).mean())

    def __setRsi(self):
        self._rsi = 100.0 - (100.0 / (1.0 + self.__rs))
