"""
This type stub file was generated by pyright.
"""

import pandas as pd
from datetime import datetime
from typing import Optional, Tuple, Union
from openbb_terminal.decorators import log_start_end

"""Nhits View"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_nhits_forecast(data: Union[pd.Series, pd.DataFrame], target_column: str = ..., dataset_name: str = ..., n_predict: int = ..., past_covariates: Optional[str] = ..., train_split: float = ..., forecast_horizon: int = ..., input_chunk_length: int = ..., output_chunk_length: int = ..., num_stacks: int = ..., num_blocks: int = ..., num_layers: int = ..., layer_widths: int = ..., pooling_kernel_sizes: Optional[Tuple[Tuple[int]]] = ..., n_freq_downsample: Optional[Tuple[Tuple[int]]] = ..., dropout: float = ..., activation: str = ..., max_pool_1d: bool = ..., batch_size: int = ..., n_epochs: int = ..., learning_rate: float = ..., model_save_name: str = ..., force_reset: bool = ..., save_checkpoints: bool = ..., export: str = ..., sheet_name: Optional[str] = ..., residuals: bool = ..., forecast_only: bool = ..., start_date: Optional[datetime] = ..., end_date: Optional[datetime] = ..., naive: bool = ..., export_pred_raw: bool = ..., metric: str = ..., external_axes: bool = ...): # -> OpenBBFigure | None:
    """Display Nhits forecast

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
    input_chunk_length: int
        Number of past time steps that are fed to the forecasting module at prediction time. Defaults to 14.
    output_chunk_length: int
        The length of the forecast of the model. Defaults to 5.
    num_stacks: int
        The number of stacks that make up the whole model.
    num_blocks: int
        The number of blocks making up every stack.
    num_layers: int
        The number of fully connected layers preceding the final forking layers in each block
        of every stack.
    layer_widths: int
        Determines the number of neurons that make up each fully connected layer in each
        block of every stack. If a list is passed, it must have a length equal to num_stacks
        and every entry in that list corresponds to the layer width of the corresponding stack.
        If an integer is passed, every stack will have blocks with FC layers of the same width.
    pooling_kernel_size: Optional[Tuple[Tuple[int]]]
        If set, this parameter must be a tuple of tuples, of size (num_stacks x num_blocks),
        specifying the kernel size for each block in each stack used for the input pooling
        layer. If left to None, some default values will be used based on input_chunk_length.
    n_freq_downsample: Optional[Tuple[Tuple[int]]]
        If set, this parameter must be a tuple of tuples, of size (num_stacks x num_blocks),
        specifying the downsampling factors before interpolation, for each block in each stack.
        If left to None, some default values will be used based on output_chunk_length.
    dropout: float
            The dropout probability to be used in fully connected layers.
    activation: str
        Supported activations: [[‘ReLU’,’RReLU’, ‘PReLU’, ‘Softplus’, ‘Tanh’, ‘SELU’, ‘LeakyReLU’, ‘Sigmoid’]
    max_pool_1d: bool
        Use max_pool_1d pooling. False uses AvgPool1d.
    batch_size: int
        Number of time series (input and output sequences) used in each training pass. Defaults to 32.
    n_epochs: int
        Number of epochs over which to train the model. Defaults to 100.
    learning_rate: float
        Defaults to 1e-3.
    model_save_name: str
        Name for model. Defaults to "brnn_model".
    force_reset: bool
        If set to True, any previously-existing model with the same name will be reset
        (all checkpoints will be discarded). Defaults to True.
    save_checkpoints: bool
        Whether or not to automatically save the untrained model and checkpoints from training.
        Defaults to True.
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
    export_pred_raw: bool
        Whether to export the raw predicted values. Defaults to False.
    metric: str
        Metric to use for evaluation. Defaults to "mape".
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

