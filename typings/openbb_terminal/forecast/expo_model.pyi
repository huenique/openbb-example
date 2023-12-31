"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import List, Optional, Tuple, Union
from darts import TimeSeries
from darts.models import ExponentialSmoothing
from numpy import ndarray
from openbb_terminal.decorators import log_start_end

"""Probabilistic Exponential Smoothing Model"""
__docformat__ = ...
TRENDS = ...
SEASONS = ...
PERIODS = ...
DAMPEN = ...
logger = ...
@log_start_end(log=logger)
def get_expo_data(data: Union[pd.Series, pd.DataFrame], target_column: str = ..., trend: str = ..., seasonal: str = ..., seasonal_periods: int = ..., dampen: str = ..., n_predict: int = ..., start_window: float = ..., forecast_horizon: int = ..., metric: str = ...) -> Tuple[List[TimeSeries], List[TimeSeries], List[TimeSeries], Optional[Union[float, ndarray]], ExponentialSmoothing,]:
    """Performs Probabilistic Exponential Smoothing forecasting
    This is a wrapper around statsmodels Holt-Winters' Exponential Smoothing;
    we refer to this link for the original and more complete documentation of the parameters.

    https://unit8co.github.io/darts/generated_api/darts.models.forecasting.exponential_smoothing.html

    Parameters
    ----------
    data : Union[pd.Series, np.ndarray]
        Input data.
    target_column: Optional[str]:
        Target column to forecast. Defaults to "close".
    trend: str
        Trend component.  One of [N, A, M]
        Defaults to ADDITIVE.
    seasonal: str
        Seasonal component.  One of [N, A, M]
        Defaults to ADDITIVE.
    seasonal_periods: int
        Number of seasonal periods in a year (7 for daily data)
        If not set, inferred from frequency of the series.
    dampen: str
        Dampen the function
    n_predict: int
        Number of days to forecast
    start_window: float
        Size of sliding window from start of timeseries and onwards
    forecast_horizon: int
        Number of days to forecast when backtesting and retraining historical
    metric: str
        Metric to use for backtesting. Defaults to MAPE.

    Returns
    -------
    Tuple[List[TimeSeries], List[TimeSeries], List[TimeSeries], Optional[Union[float, ndarray]], ExponentialSmoothing]
        Adjusted Data series,
        List of historical fcast values,
        List of predicted fcast values,
        Optional[float] - precision,
        Fit Prob. Expo model object.
    """
    ...

