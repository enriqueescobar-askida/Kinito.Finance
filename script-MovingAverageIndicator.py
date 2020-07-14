from Common.Plotters.TechIndicators.MovingAverageIndicatorPlotter import MovingAverageIndicatorPlotter
from Common.StockOptions.Yahoo.YahooStockOption import YahooStockOption
from Common.TechIndicators.MovingAverageIndicator import MovingAverageIndicator

yahooStockOption: YahooStockOption = YahooStockOption('CNI')
print(yahooStockOption.HistoricalData.describe(include='all'))
yahooStockIndicator: MovingAverageIndicator = MovingAverageIndicator(yahooStockOption)
print(yahooStockIndicator._Label)
yahooStockIndicatorPlotter: MovingAverageIndicatorPlotter =\
    MovingAverageIndicatorPlotter(yahooStockOption, yahooStockIndicator).Plot()
yahooStockIndicatorPlotter.show()
