import os
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from dotenv import load_dotenv

class StockDataFetcher:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        self.ts = TimeSeries(key=self.api_key)

    def fetch_daily_data(self, symbol, output_size='full'):
        """
        Fetch daily stock price data for a given symbol
        
        Args:
            symbol (str): Stock ticker symbol
            output_size (str): 'compact' or 'full' data
        
        Returns:
            pd.DataFrame: Processed stock price data
        """
        data, _ = self.ts.get_daily(symbol=symbol, outputsize=output_size)
        df = pd.DataFrame.from_dict(data, orient='index')
        df.index = pd.to_datetime(df.index)
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df = df.apply(pd.to_numeric)
        
        return df

    def save_data(self, df, symbol):
        """
        Save fetched data to CSV
        
        Args:
            df (pd.DataFrame): Stock price data
            symbol (str): Stock ticker symbol
        """
        os.makedirs('data/raw', exist_ok=True)
        df.to_csv(f'data/raw/{symbol}_daily.csv')