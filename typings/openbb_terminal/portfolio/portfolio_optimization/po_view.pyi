"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end
from openbb_terminal.portfolio.portfolio_optimization.po_engine import PoEngine

"""Optimization View"""
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def display_ef(portfolio_engine: Optional[PoEngine] = ..., **kwargs): # -> None:
    """Display efficient frontier

    Parameters
    ----------
    portfolio_engine : PoEngine, optional
        Portfolio optimization engine, by default None
        Use `portfolio.po.load` to load a portfolio engine
    interval : str, optional
        Interval to get data, by default '3y'
    start_date : str, optional
        If not using interval, start date string (YYYY-MM-DD), by default ""
    end_date : str, optional
        If not using interval, end date string (YYYY-MM-DD). If empty use last weekday, by default ""
    log_returns : bool, optional
        If True use log returns, else arithmetic returns, by default False
    freq : str, optional
        Frequency of returns, by default 'D'. Options: 'D' for daily, 'W' for weekly, 'M' for monthly
    maxnan: float, optional
        Maximum percentage of NaNs allowed in the data, by default 0.05
    threshold: float, optional
        Value used to replace outliers that are higher than threshold, by default 0.0
    method: str, optional
        Method used to fill nan values, by default 'time'
        For more information see `interpolate <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html>`__.
    value : float, optional
        Amount to allocate to portfolio in long positions, by default 1.0
    value_short : float, optional
        Amount to allocate to portfolio in short positions, by default 0.0
    risk_measure: str, optional
        The risk measure used to optimize the portfolio, by default 'MV'
        Possible values are:

        - 'MV': Standard Deviation.
        - 'MAD': Mean Absolute Deviation.
        - 'MSV': Semi Standard Deviation.
        - 'FLPM': First Lower Partial Moment (Omega Ratio).
        - 'SLPM': Second Lower Partial Moment (Sortino Ratio).
        - 'CVaR': Conditional Value at Risk.
        - 'EVaR': Entropic Value at Risk.
        - 'WR': Worst Realization.
        - 'ADD': Average Drawdown of uncompounded cumulative returns.
        - 'UCI': Ulcer Index of uncompounded cumulative returns.
        - 'CDaR': Conditional Drawdown at Risk of uncompounded cumulative returns.
        - 'EDaR': Entropic Drawdown at Risk of uncompounded cumulative returns.
        - 'MDD': Maximum Drawdown of uncompounded cumulative returns.

    risk_free_rate: float, optional
        Risk free rate, annualized. Used for 'FLPM' and 'SLPM' and Sharpe objective function, by default 0.0
    alpha: float, optional
        Significance level of VaR, CVaR, EDaR, DaR, CDaR, EDaR, Tail Gini of losses, by default 0.05
    n_portfolios: int, optional
        Number of portfolios to simulate, by default 100
    seed: int, optional
        Seed used to generate random portfolios, by default 123

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> d = {
                "SECTOR": {
                    "AAPL": "INFORMATION TECHNOLOGY",
                    "MSFT": "INFORMATION TECHNOLOGY",
                    "AMZN": "CONSUMER DISCRETIONARY",
                },
                "CURRENT_INVESTED_AMOUNT": {
                    "AAPL": "100000.0",
                    "MSFT": "200000.0",
                    "AMZN": "300000.0",
                },
                "CURRENCY": {
                    "AAPL": "USD",
                    "MSFT": "USD",
                    "AMZN": "USD",
                },
            }
    >>> p = openbb.portfolio.po.load(symbols_categories=d)
    >>> openbb.portfolio.po.ef_chart(portfolio_engine=p)

    >>> from openbb_terminal.sdk import openbb
    >>> p = openbb.portfolio.po.load(symbols_file_path="openbb_terminal/miscellaneous/portfolio_examples/allocation/60_40_Portfolio.xlsx")
    >>> openbb.portfolio.po.ef_chart(portfolio_engine=p)
    """
    ...

@log_start_end(log=logger)
def display_plot(portfolio_engine: Optional[PoEngine] = ..., chart_type: str = ..., **kwargs): # -> None:
    """
    Display efficient frontier

    Parameters
    ----------
    portfolio_engine : PoEngine, optional
        Portfolio optimization engine, by default None
        Use `portfolio.po.load` to load a portfolio engine
    chart_type : str, optional
        Chart type, by default "pie"
        Options are "pie", "hist", "dd" or "rc"

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> d = {
                "SECTOR": {
                    "AAPL": "INFORMATION TECHNOLOGY",
                    "MSFT": "INFORMATION TECHNOLOGY",
                    "AMZN": "CONSUMER DISCRETIONARY",
                },
                "CURRENT_INVESTED_AMOUNT": {
                    "AAPL": "100000.0",
                    "MSFT": "200000.0",
                    "AMZN": "300000.0",
                },
                "CURRENCY": {
                    "AAPL": "USD",
                    "MSFT": "USD",
                    "AMZN": "USD",
                },
            }
    >>> p = openbb.portfolio.po.load(symbols_categories=d)
    >>> weights, performance = openbb.portfolio.po.equal(portfolio_engine=p)
    >>> p.get_available_categories()
    ['SECTOR', 'CURRENCY']
    >>> openbb.portfolio.po.plot(portfolio_engine=p, category="SECTOR", chart_type="pie")
    >>> openbb.portfolio.po.plot(portfolio_engine=p, category="SECTOR", chart_type="hist")
    >>> openbb.portfolio.po.plot(portfolio_engine=p, category="SECTOR", chart_type="dd")
    >>> openbb.portfolio.po.plot(portfolio_engine=p, category="SECTOR", chart_type="rc")
    >>> openbb.portfolio.po.plot(portfolio_engine=p, category="SECTOR", chart_type="heat")

    >>> from openbb_terminal.sdk import openbb
    >>> p = openbb.portfolio.po.load(symbols_file_path="openbb_terminal/miscellaneous/portfolio_examples/allocation/60_40_Portfolio.xlsx")
    >>> weights, performance = openbb.portfolio.po.equal(portfolio_engine=p)
    >>> p.get_available_categories()
    ['ASSET_CLASS',
     'SECTOR',
     'INDUSTRY',
     'COUNTRY',
     'CURRENCY']
    >>> openbb.portfolio.po.plot(portfolio_engine=p, category="ASSET_CLASS", chart_type="pie")
    >>> openbb.portfolio.po.plot(portfolio_engine=p, category="SECTOR", chart_type="hist")
    >>> openbb.portfolio.po.plot(portfolio_engine=p, category="INDUSTRY", chart_type="dd")
    >>> openbb.portfolio.po.plot(portfolio_engine=p, category="COUNTRY", chart_type="rc")
    >>> openbb.portfolio.po.plot(portfolio_engine=p, category="ASSET_CLASS", chart_type="heat")
    """
    ...

@log_start_end(log=logger)
def display_heat(**kwargs): # -> None:
    ...

@log_start_end(log=logger)
def display_rc(**kwargs): # -> None:
    ...

@log_start_end(log=logger)
def display_hist(**kwargs): # -> None:
    ...

@log_start_end(log=logger)
def display_dd(**kwargs): # -> None:
    ...

@log_start_end(log=logger)
def display_pie(**kwargs): # -> None:
    """Show a pie chart of holdings

    Parameters
    ----------
    weights: dict
        Weights to display, where keys are tickers, and values are either weights or values if -v specified
    title: str
        Title to be used on the plot title
    external_axes:Optional[List[plt.Axes]]
        Optional external axes to plot data on
    """
    ...

@log_start_end(log=logger)
def my_autopct(x): # -> str:
    """Function for autopct of plt.pie.  This results in values not being printed in the pie if they are 'too small'"""
    ...

