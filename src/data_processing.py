import pandas as pd
import numpy as np

class StockDataProcessor:
    @staticmethod
    def calculate_returns(df):
        """
        Calculate daily returns
        
        Args:
            df (pd.DataFrame): Stock price data
        
        Returns:
            pd.Series: Daily returns
        """
        return df['close'].pct_change()

    @staticmethod
    def calculate_moving_averages(df, windows=[20, 50, 200]):
        """
        Calculate moving averages
        
        Args:
            df (pd.DataFrame): Stock price data
            windows (list): Moving average window sizes
        
        Returns:
            pd.DataFrame: DataFrame with moving averages
        """
        for window in windows:
            df[f'MA_{window}'] = df['close'].rolling(window=window).mean()
        return df

    @staticmethod
    def calculate_volatility(df, window=20):
        """
        Calculate rolling volatility
        
        Args:
            df (pd.DataFrame): Stock price data
            window (int): Rolling window size
        
        Returns:
            pd.Series: Rolling volatility
        """
        return df['close'].pct_change().rolling(window=window).std() * np.sqrt(252)