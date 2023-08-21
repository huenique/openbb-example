"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import List, Optional, Tuple, Union
from darts import TimeSeries
from darts.models import RegressionModel
from openbb_terminal.decorators import log_start_end

"""Regression Model"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def get_regression_data(data: Union[pd.Series, pd.DataFrame], target_column: str = ..., n_predict: int = ..., past_covariates: Optional[str] = ..., train_split: float = ..., forecast_horizon: int = ..., output_chunk_length: int = ..., lags: Union[int, List[int]] = ..., metric: str = ...) -> Tuple[List[TimeSeries], List[TimeSeries], List[TimeSeries], float, type[RegressionModel]]:
    """Perform Regression Forecasting

    Parameters
    ----------
    data: Union[pd.Series, pd.DataFrame]
        Input Data
    n_predict: int
        Days to predict. Defaults to 5.
    target_column: str
        Target column to forecast. Defaults to "close".
    train_split: float
        Train/val split. Defaults to 0.85.
    past_covariates: str
        Multiple secondary columns to factor in when forecasting. Defaults to None.
    forecast_horizon: int
        Forecast horizon when performing historical forecasting. Defaults to 5.
    output_chunk_length: int
        The length of the forecast of the model. Defaults to 1.
    lags: Union[int, List[int]]
        lagged target values to predict the next time step
    metric: str
        Metric to use for evaluation. Defaults to "mape".

    Returns
    -------
    Tuple[List[TimeSeries], List[TimeSeries], List[TimeSeries], float, type[RegressionModel]]
        Adjusted Data series,
        Historical forecast by best RNN model,
        list of Predictions,
        Mean average precision error,
        Best Regression Model.
    """
    ...

