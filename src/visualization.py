import matplotlib.pyplot as plt
import seaborn as sns

class StockVisualizer:
    @staticmethod
    def plot_price_trends(df, title='Stock Price Trends'):
        """
        Create comprehensive stock price visualization
        
        Args:
            df (pd.DataFrame): Stock price data
            title (str): Plot title
        """
        plt.figure(figsize=(15, 8))
        plt.plot(df.index, df['close'], label='Close Price')
        plt.plot(df.index, df['MA_20'], label='20-day MA')
        plt.plot(df.index, df['MA_50'], label='50-day MA')
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.tight_layout()
        plt.savefig('stock_trends.png')
        plt.close()

    @staticmethod
    def plot_returns_distribution(returns, title='Returns Distribution'):
        """
        Visualize returns distribution
        
        Args:
            returns (pd.Series): Stock returns
            title (str): Plot title
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(returns, kde=True)
        plt.title(title)
        plt.xlabel('Returns')
        plt.ylabel('Frequency')
        plt.savefig('returns_distribution.png')
        plt.close()