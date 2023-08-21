"""
This type stub file was generated by pyright.
"""

import numpy as np
import pandas as pd
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, Union
from openbb_terminal.decorators import log_start_end

"""Forecast Model"""
__docformat__ = ...
logger = ...
def get_default_files() -> Dict[str, Path]:
    """Get the default files to load.

    Returns
    -------
    default_files : Dict[str, Path]
        A dictionary to map the default file names to their paths.
    """
    ...

@log_start_end(log=logger)
def get_options(datasets: Dict[str, pd.DataFrame], dataset_name: Optional[str] = ...) -> Dict[Union[str, Any], pd.DataFrame]:
    """Obtain columns-dataset combinations from loaded in datasets that can be used in other commands

    Parameters
    ----------
    datasets: dict
        The available datasets.
    dataset_name: str
        The dataset you wish to show the options for.

    Returns
    -------
    option_tables: Dict[Union[str, Any], pd.DataFrame]
        A dictionary with a DataFrame for each option. With dataset_name set, only shows one
        options table.
    """
    ...

@log_start_end(log=logger)
def clean(dataset: pd.DataFrame, fill: Optional[str] = ..., drop: Optional[str] = ..., limit: Optional[int] = ...) -> Tuple[pd.DataFrame, np.bool_]:
    """Clean up NaNs from the dataset

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset you wish to clean
    fill : Optional[str]
        The method of filling NaNs
    drop : Optional[str]
        The method of dropping NaNs
    limit : Optional[int]
        The maximum limit you wish to apply that can be forward or backward filled

    Returns
    -------
    Tuple[pd.DataFrame, np.bool_]
        The cleaned dataset and a boolean indicating if there are any NaNs left
    """
    ...

@log_start_end(log=logger)
def add_ema(dataset: pd.DataFrame, target_column: str = ..., period: int = ...) -> pd.DataFrame:
    """A moving average provides an indication of the trend of the price movement
    by cut down the amount of "noise" on a price chart.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset you wish to clean
    target_column : str
        The column you wish to add the EMA to
    period : int
        Time Span

    Returns
    -------
    pd.DataFrame
        Dataframe with added EMA column
    """
    ...

@log_start_end(log=logger)
def add_sto(dataset: pd.DataFrame, close_column: str = ..., high_column: str = ..., low_column: str = ..., period: int = ...) -> pd.DataFrame:
    """Stochastic Oscillator %K and %D : A stochastic oscillator is a momentum indicator comparing a particular closing
    price of a security to a range of its prices over a certain period of time. %K and %D are slow and fast indicators.

    Requires Low/High/Close columns.
    Note: This will drop first rows equal to period due to how this metric is calculated.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset you wish to calculate for
    period : int
        Span of time to calculate over
    close_column : str
        The column name for the close price
    high_column : str
        The column name for the high price
    low_column : str
        The column name for the low price

    Returns
    -------
    pd.DataFrame
        Dataframe with added STO K & D columns
    """
    ...

@log_start_end(log=logger)
def add_rsi(dataset: pd.DataFrame, target_column: str = ..., period: int = ...) -> pd.DataFrame:
    """A momentum indicator that measures the magnitude of recent price changes to evaluate
    overbought or oversold conditions in the price of a stock or other asset.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset you wish to calculate for
    target_column : str
        The column you wish to add the RSI to
    period : int
        Time Span

    Returns
    -------
    pd.DataFrame
        Dataframe with added RSI column
    """
    ...

@log_start_end(log=logger)
def add_roc(dataset: pd.DataFrame, target_column: str = ..., period: int = ...) -> pd.DataFrame:
    """A momentum oscillator, which measures the percentage change between the current
    value and the n period past value.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset you wish to calculate with
    target_column : str
        The column you wish to add the ROC to
    period : int
        Time Span

    Returns
    -------
    pd.DataFrame
        Dataframe with added ROC column
    """
    ...

@log_start_end(log=logger)
def add_momentum(dataset: pd.DataFrame, target_column: str = ..., period: int = ...) -> pd.DataFrame:
    """A momentum oscillator, which measures the percentage change between the current
    value and the n period past value.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset you wish to calculate with
    target_column : str
        The column you wish to add the MOM to
    period : int
        Time Span

    Returns
    -------
    pd.DataFrame
        Dataframe with added MOM column
    """
    ...

@log_start_end(log=logger)
def add_delta(dataset: pd.DataFrame, target_column: str = ...) -> pd.DataFrame:
    """
    Calculate the %change of a variable based on a specific column
    """
    ...

@log_start_end(log=logger)
def add_atr(dataset: pd.DataFrame, close_column: str = ..., high_column: str = ..., low_column: str = ...) -> pd.DataFrame:
    """
    Calculate the Average True Range of a variable based on a a specific stock ticker.
    """
    ...

@log_start_end(log=logger)
def add_signal(dataset: pd.DataFrame, target_column: str = ...) -> pd.DataFrame:
    """A price signal based on short/long term price.

    1 if the signal is that short term price will go up as compared to the long term.
    0 if the signal is that short term price will go down as compared to the long term.

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset you wish to calculate with

    Returns
    -------
    pd.DataFrame
        Dataframe with added signal column
    """
    ...

@log_start_end(log=logger)
def combine_dfs(df1: pd.DataFrame, df2: pd.DataFrame, column: str, dataset: str = ...) -> pd.DataFrame:
    """Adds the given column of df2 to df1

    Parameters
    ----------
    df1: pd.DataFrame
        The dataframe to add a column to
    df2: pd.DataFrame
        The dataframe to lose a column
    column: str
        The column to transfer
    dataset: str
        A name for df2 (shows in name of new column)

    Returns
    -------
    data: pd.DataFrame
        The new dataframe
    """
    ...

@log_start_end(log=logger)
def delete_column(data: pd.DataFrame, column: str) -> None:
    """Delete a column from a dataframe

    Parameters
    ----------
    data : pd.DataFrame
        The dataframe to delete a column from
    column : str
        The column to delete

    Returns
    -------
    None
    """
    ...

@log_start_end(log=logger)
def rename_column(data: pd.DataFrame, old_column: str, new_column: str) -> pd.DataFrame:
    """Rename a column in a dataframe

    Parameters
    ----------
    data: pd.DataFrame
        The dataframe to have a column renamed
    old_column: str
        The column that will have its name changed
    new_column: str
        The name to update to

    Returns
    -------
    new_df: pd.DataFrame
        The dataframe with the renamed column
    """
    ...

@log_start_end(log=logger)
def describe_df(data: pd.DataFrame) -> pd.DataFrame:
    """Returns statistics for a given df

    Parameters
    ----------
    data: pd.DataFrame
        The df to produce statistics for

    Returns
    -------
    df: pd.DataFrame
        The df with the new data
    """
    ...

@log_start_end(log=logger)
def corr_df(data: pd.DataFrame) -> pd.DataFrame:
    """Returns correlation for a given df

    Parameters
    ----------
    data: pd.DataFrame
        The df to produce statistics for

    Returns
    -------
    df: pd.DataFrame
        The df with the new data
    """
    ...

