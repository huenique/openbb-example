"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Tuple
from openbb_terminal.decorators import log_start_end

""" ECB model """
__docformat__ = ...
logger = ...
@log_start_end(log=logger)
def get_series_data(series_id: str = ..., start_date: str = ..., end_date: str = ...): # -> DataFrame:
    """Get ECB data

    Parameters
    ----------
    series_id: str
        ECB ID of data
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    """
    ...

@log_start_end(log=logger)
def get_ecb_yield_curve(date: str = ..., yield_type: str = ..., return_date: bool = ..., detailed: bool = ..., any_rating: bool = ...) -> Tuple[pd.DataFrame, str]:
    """Gets euro area yield curve data from ECB.

    The graphic depiction of the relationship between the yield on bonds of the same credit quality but different
    maturities is known as the yield curve. In the past, most market participants have constructed yield curves from
    the observations of prices and yields in the Treasury market. Two reasons account for this tendency. First,
    Treasury securities are viewed as free of default risk, and differences in creditworthiness do not affect yield
    estimates. Second, as the most active bond market, the Treasury market offers the fewest problems of illiquidity
    or infrequent trading. The key function of the Treasury yield curve is to serve as a benchmark for pricing bonds
    and setting yields in other sectors of the debt market.

    It is clear that the market’s expectations of future rate changes are one important determinant of the
    yield-curve shape. For example, a steeply upward-sloping curve may indicate market expectations of near-term Fed
    tightening or of rising inflation. However, it may be too restrictive to assume that the yield differences across
    bonds with different maturities only reflect the market’s rate expectations. The well-known pure expectations
    hypothesis has such an extreme implication. The pure expectations hypothesis asserts that all government bonds
    have the same near-term expected return (as the nominally riskless short-term bond) because the return-seeking
    activity of risk-neutral traders removes all expected return differentials across bonds.

    Parameters
    ----------
    date: str
        Date to get curve for. If empty, gets most recent date (format yyyy-mm-dd)
    yield_type: str
        What type of yield curve to get, options: ['spot_rate', 'instantaneous_forward', 'par_yield']
    return_date: bool
        If True, returns date of yield curve
    detailed: bool
        If True, returns detailed data. Note that this is very slow.
    aaa_only: bool
        If True, it only returns rates for AAA rated bonds. If False, it returns rates for all bonds

    Returns
    -------
    Tuple[pd.DataFrame, str]
        Dataframe of yields and maturities,
        Date for which the yield curve is obtained

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> ycrv_df = openbb.fixedincome.ycrv()

    Since there is a delay with the data, the most recent date is returned and can be accessed with return_date=True
    >>> ycrv_df, ycrv_date = openbb.fixedincome.ycrv(return_date=True)
    """
    ...

