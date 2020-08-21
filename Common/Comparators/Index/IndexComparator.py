import numpy as np
from sklearn.preprocessing import MinMaxScaler

from Common.Comparators.Index.AbstractIndexComparator import AbstractIndexComparator
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from sklearn import preprocessing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math


class IndexComparator(AbstractIndexComparator):

    def __init__(self, stock_option: YahooStockOption, indices: list()):
        self.__stockOption = stock_option
        self.__indexList = indices
        self.Data = self.__setComparator(indices)
        self.DataSimpleReturns = self.__setSimpleReturns(self.Data)
        self.DataSimpleReturnsCorr = self.__setSimpleReturnsCorr(self.Data)
        self.DataLogReturns = self.__setLogReturns(self.Data)
        self.DataNormalized = self.__setNormalizer()
        self.DataScaled = self.__setScaler()
        self.__summaryPlot(self.Data, 'Flat', 'Price in USD')
        self.__snsBoxPlot(self.Data, 'Flat', 'Price in USD')
        self.__heatMap(self.DataSimpleReturnsCorr)
        self.__summaryPlot(self.DataNormalized, 'Normalized', 'Base 1 variation since ' + stock_option.TimeSpan.StartDateStr)
        self.__snsBoxPlot(self.DataNormalized, 'Normalized', 'Base 1 variation since ' + stock_option.TimeSpan.StartDateStr)
        self.__summaryPlot(self.DataScaled, 'Scaled', 'Range [0-100] scaled since ' + stock_option.TimeSpan.StartDateStr)
        self.__snsBoxPlot(self.DataScaled, 'Scaled', 'Range [0-100] scaled since ' + stock_option.TimeSpan.StartDateStr)

    def __setComparator(self, indices):
        df: pd.DataFrame = self.__stockOption.HistoricalData[self.__stockOption.SourceColumn].to_frame()
        df.columns = self.__stockOption.Ticker + df.columns
        a_df: pd.DataFrame = indices[0].HistoricalData
        for a_index in indices[1:]:
            a_df = a_df.merge(a_index.HistoricalData, left_index=True, right_index=True)
        return df.merge(a_df, left_index=True, right_index=True)

    def __setNormalizer(self):
        return self.Data / self.Data.iloc[0]

    def __setScaler(self):
        # scale to compare array from 0.0 to 100.0
        minMaxScaler: MinMaxScaler = preprocessing.MinMaxScaler(feature_range=(0.0, 100.0))
        # scale to compare data frame
        stockArrayScaled: np.ndarray = minMaxScaler.fit_transform(self.Data)
        return pd.DataFrame(stockArrayScaled, columns=self.Data.columns)

    def __setSimpleReturns(self, df: pd.DataFrame):
        return df.pct_change(1)

    def __setSimpleReturnsCorr(self, df: pd.DataFrame):
        return self.__setSimpleReturns(df).corr()

    def __setLogReturns(self, df: pd.DataFrame):
        return np.log(df/df.shift(1))

    def __snsBoxPlot(self, df: pd.DataFrame, a_title: str = '', y_title: str = ''):
        plt.figure(figsize=(3 * math.log(self.__stockOption.TimeSpan.MonthCount), 4.5))
        sns.boxplot(data=df, width=.5)#fliersize=20, whis=.2, , linewidth=2.5
        plt.title('Stock ' + self.__stockOption.SourceColumn + ' ' + a_title)
        plt.xlabel('Stock tickers')
        plt.xticks(rotation=45)
        plt.ylabel(y_title)
        plt.show()

    def __summaryPlot(self, df: pd.DataFrame, a_title: str = '', y_title: str = ''):
        plt.figure(figsize=(3 * math.log(self.__stockOption.TimeSpan.MonthCount), 4.5))
        for c in df.columns.values:
            plt.plot(df.index, df[c], lw=2, label=c)
        plt.title(self.__stockOption.SourceColumn + ' ' + a_title + ' ' + str(self.__stockOption.TimeSpan.MonthCount) + ' months')
        plt.xlabel(self.__stockOption.TimeSpan.StartDateStr + ' - ' + self.__stockOption.TimeSpan.EndDateStr)
        plt.ylabel(y_title)
        plt.legend(loc='upper left', fontsize=10)
        plt.show()

    def __heatMap(self, df: pd.DataFrame):
        fig_size = 1.75 * math.log(self.__stockOption.TimeSpan.MonthCount)
        plt.subplots(figsize=(fig_size, fig_size))
        s_h_m = sns.heatmap(df, cmap="RdYlGn", annot=True, fmt='.2%')  # YlOrRd
        s_h_m.set_xticklabels(s_h_m.get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.show()
        sns.clustermap(df, cmap="coolwarm", row_cluster=True, col_cluster=False)
        plt.show()
