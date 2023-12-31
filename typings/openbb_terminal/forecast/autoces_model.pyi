"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import List, Optional, Tuple, Union
from darts import TimeSeries
from statsforecast.core import StatsForecast
from openbb_terminal.decorators import log_start_end

"""Automatic Comples Exponential Smoothing Model"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def get_autoces_data(data: Union[pd.Series, pd.DataFrame], target_column: str = ..., seasonal_periods: int = ..., n_predict: int = ..., start_window: float = ..., forecast_horizon: int = ...) -> Tuple[Optional[List[type[TimeSeries]]], Optional[List[type[TimeSeries]]], Optional[List[type[TimeSeries]]], Optional[float], Optional[StatsForecast],]:
    """Performs Automatic Complex Exponential Smoothing forecasting
    This is a wrapper around StatsForecast AutoCES;
    we refer to this link for the original and more complete documentation of the parameters.


        https://nixtla.github.io/statsforecast/models.html#autoces

    Parameters
    ----------
    data : Union[pd.Series, np.ndarray]
        Input data.
    target_column: Optional[str]:
        Target column to forecast. Defaults to "close".
    seasonal_periods: int
        Number of seasonal periods in a year (7 for daily data)
        If not set, inferred from frequency of the series.
    n_predict: int
        Number of days to forecast
    start_window: float
        Size of sliding window from start of timeseries and onwards
    forecast_horizon: int
        Number of days to forecast when backtesting and retraining historical

    Returns
    -------
    Tuple[List[TimeSeries], List[TimeSeries], List[TimeSeries], Optional[float], StatsForecast]
        Adjusted Data series,
        List of historical fcast values,
        List of predicted fcast values,
        Optional[float] - precision,
        Fit CES model object.
    """
    ...

