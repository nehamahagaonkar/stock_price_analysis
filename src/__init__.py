from src.data_acquisition import StockDataFetcher
from src.data_processing import StockDataProcessor
from src.analysis import StockAnalyzer
from src.visualization import StockVisualizer

def main():
    # Fetch stock data
    fetcher = StockDataFetcher()
    aapl_data = fetcher.fetch_daily_data('AAPL')
    fetcher.save_data(aapl_data, 'AAPL')

    # Process data
    processor = StockDataProcessor()
    aapl_data = processor.calculate_moving_averages(aapl_data)
    returns = processor.calculate_returns(aapl_data)

    # Analyze data
    analyzer = StockAnalyzer()
    trend = analyzer.trend_detection(aapl_data)

    # Visualize
    visualizer = StockVisualizer()
    visualizer.plot_price_trends(aapl_data)
    visualizer.plot_returns_distribution(returns)

if __name__ == '__main__':
    main()