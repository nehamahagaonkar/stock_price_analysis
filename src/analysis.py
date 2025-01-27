import pandas as pd
import numpy as np
from scipy import stats

class StockAnalyzer:
    @staticmethod
    def correlation_analysis(data1, data2):
        """
        Perform correlation analysis between two stocks
        
        Args:
            data1 (pd.Series): First stock returns
            data2 (pd.Series): Second stock returns
        
        Returns:
            dict: Correlation metrics
        """
        correlation = data1.corr(data2)
        p_value = stats.pearsonr(data1, data2)[1]
        
        return {
            'correlation': correlation,
            'p_value': p_value
        }

    @staticmethod
    def trend_detection(df, window=20):
        """
        Detect market trends using moving averages
        
        Args:
            df (pd.DataFrame): Stock price data
            window (int): Trend detection window
        
        Returns:
            pd.Series: Trend indicators
        """
        short_ma = df['close'].rolling(window=window).mean()
        long_ma = df['close'].rolling(window=window*2).mean()
        
        df['trend'] = np.where(short_ma > long_ma, 1, -1)
        return df['trend']