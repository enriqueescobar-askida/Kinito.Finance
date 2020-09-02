import math
import matplotlib.pyplot as plt
from Common.Plotters.Strategies.AbstractStrategyPlotter import AbstractStrategyPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.Strategies.TechIndicators.MacdStrategy import MacdStrategy


class MacdStrategyPlotter(AbstractStrategyPlotter):

    def __init__(self, y_stock_option: YahooStockOption, macd_strategy: MacdStrategy):
        self.__FIG_SIZE = (3 * math.log(y_stock_option.TimeSpan.MonthCount), 4.5)
        self.__LEGEND_PLACE = 'upper left'
        self.__PLOT_STYLE = 'fivethirtyeight'
        self.__SOURCE = y_stock_option.Source
        self.__TICKER = y_stock_option.Ticker
        self.__TICKER_LABEL = y_stock_option.Source + y_stock_option.Ticker + "_" + macd_strategy._Col
        self.__TITLE = "{0}{1}_{2} {3} History {4} BUY & SELL Signals".format(y_stock_option.Source,
                                                                              y_stock_option.Ticker,
                                                                              macd_strategy._Label,
                                                                              macd_strategy._Col,
                                                                              macd_strategy._Label)
        self.__XLABEL = y_stock_option.TimeSpan.StartDateStr + ' - ' + y_stock_option.TimeSpan.EndDateStr
        self.__XTICKS_ANGLE = 45
        self.__YLABEL = macd_strategy._Col + ' in $USD'
        self.__DATE_TIME_INDEX = y_stock_option.HistoricalData.index
        self.__STRATEGY_DATA_FRAME = macd_strategy._DataFrame
        self.__STRATEGY_LABEL = macd_strategy._Label
        self.__STRATEGY_LABEL_BUY = macd_strategy._BuyLabel
        self.__STRATEGY_DATA_BUY = macd_strategy._DataFrame[macd_strategy._BuyLabel]
        self.__STRATEGY_LABEL_SELL = macd_strategy._SellLabel
        self.__STRATEGY_DATA_SELL = macd_strategy._DataFrame[macd_strategy._SellLabel]

    def Plot(self):
        # plt.style.use(self.__PLOT_STYLE)
        plt.figure(figsize=self.__FIG_SIZE)
        plt.plot(self.__STRATEGY_DATA_FRAME[self.__TICKER], label=self.__TICKER_LABEL, alpha=0.6)
        plt.scatter(self.__DATE_TIME_INDEX, self.__STRATEGY_DATA_BUY, label=self.__STRATEGY_LABEL_BUY, marker='^', color='green')
        plt.scatter(self.__DATE_TIME_INDEX, self.__STRATEGY_DATA_SELL, label=self.__STRATEGY_LABEL_SELL, marker='v', color='red')
        plt.title(self.__TITLE)
        plt.xlabel(self.__XLABEL)
        plt.xticks(rotation=self.__XTICKS_ANGLE)
        plt.ylabel(self.__YLABEL)
        plt.legend(loc=self.__LEGEND_PLACE)
        return plt
