"""
This type stub file was generated by pyright.
"""

import pandas as pd
from datetime import datetime
from typing import List, Optional, Union
from openbb_terminal.decorators import log_start_end

""" Regression View"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_regression(data: Union[pd.Series, pd.DataFrame], target_column: str = ..., dataset_name: str = ..., n_predict: int = ..., past_covariates: Optional[str] = ..., train_split: float = ..., forecast_horizon: int = ..., output_chunk_length: int = ..., lags: Union[int, List[int]] = ..., export: str = ..., sheet_name: Optional[str] = ..., residuals: bool = ..., forecast_only: bool = ..., start_date: Optional[datetime] = ..., end_date: Optional[datetime] = ..., naive: bool = ..., explainability_raw: bool = ..., export_pred_raw: bool = ..., metric: str = ..., external_axes: bool = ...): # -> OpenBBFigure | None:
    """Display Regression Forecasting

    Parameters
    ----------
    data: Union[pd.Series, pd.DataFrame]
        Input Data
    target_column: str
        Target column to forecast. Defaults to "close".
    dataset_name: str
        The name of the ticker to be predicted
    n_predict: int
        Days to predict. Defaults to 5.
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
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export data
    residuals: bool
        Whether to show residuals for the model. Defaults to False.
    forecast_only: bool
        Whether to only show dates in the forecasting range. Defaults to False.
    start_date: Optional[datetime]
        The starting date to perform analysis, data before this is trimmed. Defaults to None.
    end_date: Optional[datetime]
        The ending date to perform analysis, data after this is trimmed. Defaults to None.
    naive: bool
        Whether to show the naive baseline. This just assumes the closing price will be the same
        as the previous day's closing price. Defaults to False.
    metric: str
        The metric to use for the forecast. Defaults to "mape".
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

