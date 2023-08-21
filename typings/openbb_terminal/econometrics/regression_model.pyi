"""
This type stub file was generated by pyright.
"""

import pandas as pd
import statsmodels
from typing import Any, Dict, List, Optional, Tuple
from pandas import DataFrame
from openbb_terminal.decorators import log_start_end

"""Regression Model"""
__docformat__ = ...
logger = ...
def get_regressions_results(Y: pd.DataFrame, X: pd.DataFrame, regression_type: str = ..., entity_effects: bool = ..., time_effects: bool = ...) -> Any:
    """Based on the regression type, this function decides what regression to run.

    Parameters
    ----------
    Y: pd.DataFrame
        Dataframe containing the dependent variable.
    X: pd.DataFrame
        Dataframe containing the independent variables.
    regression_type: str
        The type of regression you wish to execute.
    entity_effects: bool
        Whether to apply Fixed Effects on entities.
    time_effects: bool
        Whether to apply Fixed Effects on time.

    Returns
    -------
    Any
        A regression model

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.econometrics.load("wage_panel")
    >>> df = df.set_index(["nr","year"])
    >>> X = df[["exper","educ","union"]]
    >>> Y = df["lwage"]
    >>> pooled_ols_model = openbb.econometrics.panel(Y,X,"POLS")
    >>> print(pooled_ols_model.summary)
                        PooledOLS Estimation Summary
    ================================================================================
    Dep. Variable:                  lwage   R-squared:                        0.1634
    Estimator:                  PooledOLS   R-squared (Between):              0.1686
    No. Observations:                4360   R-squared (Within):               0.1575
    Date:                Sun, Nov 13 2022   R-squared (Overall):              0.1634
    Time:                        13:04:02   Log-likelihood                   -3050.4
    Cov. Estimator:            Unadjusted
                                            F-statistic:                      283.68
    Entities:                         545   P-value                           0.0000
    Avg Obs:                       8.0000   Distribution:                  F(3,4356)
    Min Obs:                       8.0000
    Max Obs:                       8.0000   F-statistic (robust):             283.68
                                            P-value                           0.0000
    Time periods:                       8   Distribution:                  F(3,4356)
    Avg Obs:                       545.00
    Min Obs:                       545.00
    Max Obs:                       545.00
                                Parameter Estimates
    ==============================================================================
                Parameter  Std. Err.     T-stat    P-value    Lower CI    Upper CI
    ------------------------------------------------------------------------------
    const         -0.0308     0.0620    -0.4965     0.6196     -0.1523      0.0908
    exper          0.0561     0.0028     20.220     0.0000      0.0507      0.0616
    educ           0.1080     0.0045     24.034     0.0000      0.0992      0.1168
    union          0.1777     0.0172     10.344     0.0000      0.1441      0.2114
    ==============================================================================
    """
    ...

def get_regression_data(regression_variables: List[tuple], data: Dict[str, pd.DataFrame], regression_type: str = ...) -> Tuple[DataFrame, Any, List[Any]]:
    """This function creates a DataFrame with the required regression data as
    well sets up the dependent and independent variables.

    Parameters
    ----------
    regression_variables : list
        The regressions variables entered where the first variable is
        the dependent variable.
    data : dict
        A dictionary containing the datasets.
    regression_type: str
        The type of regression that is executed.

    Returns
    -------
    Tuple[DataFrame, Any, List[Any]]
        The dataset used,
        Dependent variable,
        Independent variable,
        OLS model.
    """
    ...

@log_start_end(log=logger)
def get_ols(Y: pd.DataFrame, X: pd.DataFrame) -> Any:
    """Performs an OLS regression on timeseries data. [Source: Statsmodels]

    Parameters
    ----------
    Y: pd.DataFrame
        Dependent variable series.
    X: pd.DataFrame
        Dataframe of independent variables series.

    Returns
    -------
    statsmodels.regression.linear_model.RegressionResultsWrapper
        Regression model wrapper from statsmodels.

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.econometrics.load("wage_panel")
    >>> OLS_model = openbb.econometrics.ols(df["lwage"], df[["educ", "exper", "expersq"]])
    >>> print(OLS_model.summary())`
                                OLS Regression Results
    =======================================================================================
    Dep. Variable:                  lwage   R-squared (uncentered):                   0.920
    Model:                            OLS   Adj. R-squared (uncentered):              0.919
    Method:                 Least Squares   F-statistic:                          1.659e+04
    Date:                Thu, 10 Nov 2022   Prob (F-statistic):                        0.00
    Time:                        15:28:11   Log-Likelihood:                         -3091.3
    No. Observations:                4360   AIC:                                      6189.
    Df Residuals:                    4357   BIC:                                      6208.
    Df Model:                           3
    Covariance Type:            nonrobust
    ==============================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    educ           0.0986      0.002     39.879      0.000       0.094       0.103
    exper          0.1018      0.009     10.737      0.000       0.083       0.120
    expersq       -0.0034      0.001     -4.894      0.000      -0.005      -0.002
    ==============================================================================
    Omnibus:                     1249.642   Durbin-Watson:                   0.954
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):             9627.436
    Skew:                          -1.152   Prob(JB):                         0.00
    Kurtosis:                       9.905   Cond. No.                         86.4
    ==============================================================================
    Notes:
    [1] R² is computed without centering (uncentered) since the model does not contain a constant.
    [2] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    """
    ...

@log_start_end(log=logger)
def get_pols(Y: pd.DataFrame, X: pd.DataFrame) -> Any:
    """PooledOLS is just plain OLS that understands that various panel data structures.
    It is useful as a base model. [Source: LinearModels]

    Parameters
    ----------
    regression_variables : list
        The regressions variables entered where the first variable is
        the dependent variable.
    data : dict
        A dictionary containing the datasets.

    Returns
    -------
    Tuple[DataFrame, Any, List[Any], Any]
        The dataset used,
        Dependent variable,
        Independent variable,
        PooledOLS model
    """
    ...

@log_start_end(log=logger)
def get_re(Y: pd.DataFrame, X: pd.DataFrame) -> Any:
    """The random effects model is virtually identical to the pooled OLS model except that is accounts for the
    structure of the model and so is more efficient. Random effects uses a quasi-demeaning strategy which
    subtracts the time average of the within entity values to account for the common shock. [Source: LinearModels]

    Parameters
    ----------
    regression_variables : list
        The regressions variables entered where the first variable is
        the dependent variable.
    data : dict
        A dictionary containing the datasets.

    Returns
    -------
    Tuple[DataFrame, Any, List[Any], Any]
        The dataset used,
        Dependent variable,
        Independent variable,
        RandomEffects model
    """
    ...

@log_start_end(log=logger)
def get_bols(Y: pd.DataFrame, X: pd.DataFrame) -> Any:
    """The between estimator is an alternative, usually less efficient estimator, can can be used to
    estimate model parameters. It is particular simple since it first computes the time averages of
    y and x and then runs a simple regression using these averages. [Source: LinearModels]

    Parameters
    ----------
    regression_variables : list
        The regressions variables entered where the first variable is
        the dependent variable.
    data : dict
        A dictionary containing the datasets.

    Returns
    -------
    Tuple[DataFrame, Any, List[Any], Any]
        The dataset used,
        Dependent variable,
        Independent variable,
        Between OLS model.
    """
    ...

@log_start_end(log=logger)
def get_fe(Y: pd.DataFrame, X: pd.DataFrame, entity_effects: bool = ..., time_effects: bool = ...) -> Any:
    """When effects are correlated with the regressors the RE and BE estimators are not consistent.
    The usual solution is to use Fixed Effects which are called entity_effects when applied to
    entities and time_effects when applied to the time dimension. [Source: LinearModels]

    Parameters
    ----------
    regression_variables : list
        The regressions variables entered where the first variable is
        the dependent variable.
    data : dict
        A dictionary containing the datasets.
    entity_effects : bool
        Whether to include entity effects
    time_effects : bool
        Whether to include time effects

    Returns
    -------
    Tuple[DataFrame, Any, List[Any], Any]
        The dataset used,
        Dependent variable,
        Independent variable,
        PanelOLS model with Fixed Effects
    """
    ...

@log_start_end(log=logger)
def get_fdols(Y: pd.DataFrame, X: pd.DataFrame) -> Any:
    """First differencing is an alternative to using fixed effects when there might be correlation.
    When using first differences, time-invariant variables must be excluded. Additionally,
    only one linear time-trending variable can be included since this will look like a constant.
    This variable will soak up all time-trends in the data, and so interpretations of
    these variable can be challenging. [Source: LinearModels]

    Parameters
    ----------
    regression_variables : list
        The regressions variables entered where the first variable is
        the dependent variable.
    data : dict
        A dictionary containing the datasets.

    Returns
    -------
    Tuple[DataFrame, Any, List[Any], Any]
        The dataset used,
        Dependent variable,
        Independent variable,
        First Difference OLS model
    """
    ...

@log_start_end(log=logger)
def get_comparison(regressions: Dict, export: str = ..., sheet_name: Optional[str] = ...): # -> PanelModelComparison | None:
    """Compare regression results between Panel Data regressions.

    Parameters
    ----------
    regressions : Dict
        Dictionary with regression results.
    export : str
        Format to export data

    Returns
    -------
    dict
        Returns a PanelModelComparison which shows an overview of the different regression results.
    """
    ...

@log_start_end(log=logger)
def get_dwat(model: statsmodels.regression.linear_model.RegressionResultsWrapper) -> float:
    """Calculate test statistics for Durbin Watson autocorrelation

    Parameters
    ----------
    model : statsmodels.regression.linear_model.RegressionResultsWrapper
        Previously fit statsmodels OLS.

    Returns
    -------
    float
        Test statistic of the Durbin Watson test.

    Notes
    ------
    When using chart = True, the dependent variable in the regression must be passed to view the residuals

    Example
    -------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.econometrics.load("wage_panel")
    >>> Y, X = df["lwage"], df[["exper","educ"]]
    >>> model = openbb.econometrics.ols(Y,X)
    >>> durbin_watson_value = openbb.econometrics.dwat(model)
    0.96
    """
    ...

@log_start_end(log=logger)
def get_bgod(model: pd.DataFrame, lags: int = ...) -> Tuple[float, float, float, float]:
    """Calculate test statistics for autocorrelation

    Parameters
    ----------
    model : OLS Model
        OLS model that has been fit.
    lags : int
        The amount of lags.

    Returns
    -------
    pd.DataFrame
        Test results from the Breusch-Godfrey Test
    """
    ...

@log_start_end(log=logger)
def get_bpag(model: statsmodels.regression.linear_model.RegressionResultsWrapper) -> pd.DataFrame:
    """Calculate test statistics for heteroscedasticity

    Parameters
    ----------
    model : OLS Model
        Model containing residual values.

    Returns
    -------
    pd.DataFrame
        Test results from the Breusch-Pagan Test
    """
    ...
