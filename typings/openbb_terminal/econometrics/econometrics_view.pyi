"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Dict, Optional, Union
from openbb_terminal import OpenBBFigure
from openbb_terminal.decorators import log_start_end

"""Econometrics View"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def show_options(datasets: Dict[str, pd.DataFrame], dataset_name: Optional[str] = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Plot custom data

    Parameters
    ----------
    datasets: dict
        The loaded in datasets
    dataset_name: str
        The name of the dataset you wish to show options for
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export image
    """
    ...

@log_start_end(log=logger)
def display_plot(data: Union[pd.Series, pd.DataFrame, Dict[str, pd.DataFrame]], export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[None, OpenBBFigure]:
    """Plot data from a dataset

    Parameters
    ----------
    data: Union[pd.Series, pd.DataFrame, Dict[str: pd.DataFrame]
        Dictionary with key being dataset.column and dataframes being values
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export image
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
def display_corr(dataset: pd.DataFrame, export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...) -> Union[OpenBBFigure, None]:
    """Plot correlation coefficients for dataset features

    Parameters
    ----------
    dataset : pd.DataFrame
        The dataset fore calculating correlation coefficients
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export image
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
def display_norm(data: pd.Series, dataset: str = ..., column: str = ..., plot: bool = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...): # -> OpenBBFigure | None:
    """Determine the normality of a timeseries.

    Parameters
    ----------
    data: pd.Series
        Series of custom data
    dataset: str
        Dataset name
    column: str
        Column for y data
    plot : bool
        Whether you wish to plot a histogram
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export data.
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
def display_root(data: pd.Series, dataset: str = ..., column: str = ..., fuller_reg: str = ..., kpss_reg: str = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Determine the normality of a timeseries.

    Parameters
    ----------
    data : pd.Series
        Series of target variable
    dataset: str
        Name of the dataset
    column: str
        Name of the column
    fuller_reg : str
        Type of regression of ADF test. Choose c, ct, ctt, or nc
    kpss_reg : str
        Type of regression for KPSS test. Choose c or ct
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export data.
    """
    ...

@log_start_end(log=logger)
def display_garch(dataset: pd.DataFrame, column: str, p: int = ..., o: int = ..., q: int = ..., mean: str = ..., horizon: int = ..., detailed: bool = ..., export: str = ..., external_axes: bool = ...) -> Union[OpenBBFigure, None]:
    """Plots the volatility forecasts based on GARCH

    Parameters
    ----------
    dataset: pd.DataFrame
        The dataframe to use
    column: str
        The column of the dataframe to use
    p: int
        Lag order of the symmetric innovation
    o: int
        Lag order of the asymmetric innovation
    q: int
        Lag order of lagged volatility or equivalent
    mean: str
        The name of the mean model
    horizon: int
        The horizon of the forecast
    detailed: bool
        Whether to display the details about the parameter fit, for instance the confidence interval
    export: str
        Format to export data
    external_axes: bool
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
def display_granger(dependent_series: pd.Series, independent_series: pd.Series, lags: int = ..., confidence_level: float = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Show granger tests

    Parameters
    ----------
    dependent_series: Series
        The series you want to test Granger Causality for.
    independent_series: Series
        The series that you want to test whether it Granger-causes dependent_series
    lags : int
        The amount of lags for the Granger test. By default, this is set to 3.
    confidence_level: float
        The confidence level you wish to use. By default, this is set to 0.05.
    export : str
        Format to export data
    """
    ...

@log_start_end(log=logger)
def display_cointegration_test(*datasets: pd.Series, significant: bool = ..., plot: bool = ..., export: str = ..., sheet_name: Optional[str] = ..., external_axes: bool = ...): # -> OpenBBFigure | None:
    """Estimates long-run and short-run cointegration relationship for series y and x and apply
    the two-step Engle & Granger test for cointegration.

    Uses a 2-step process to first estimate coefficients for the long-run relationship
        y_t = c + gamma * x_t + z_t

    and then the short-term relationship,
        y_t - y_(t-1) = alpha * z_(t-1) + epsilon_t,

    with z the found residuals of the first equation.

    Then tests co-integration with the Dickey-Fuller phi=1 vs phi < 1 in
        z_t = phi * z_(t-1) + eta_t

    If this implies phi < 1, the z series is stationary is concluded to be
    stationary, and thus the series y and x are concluded to be cointegrated.

    Parameters
    ----------
    datasets: pd.Series
        Variable number of series to test for cointegration
    significant: float
        Show only companies that have p-values lower than this percentage
    plot: bool
        Whether you wish to plot the z-values of all pairs.
    export : str
        Format to export data
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
def display_vif(dataset: pd.DataFrame, columns: Optional[list] = ..., export: str = ..., sheet_name: Optional[str] = ...): # -> None:
    """Displays the VIF (variance inflation factor), which tests for collinearity, values for each column.

    Parameters
    ----------
    dataset: pd.Series
        Dataset to calculate VIF on
    columns: Optional[list]
        The columns to calculate to test for collinearity
    sheet_name: Optional[str]
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export data.
    """
    ...

