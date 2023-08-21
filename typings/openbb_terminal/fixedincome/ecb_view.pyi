"""
This type stub file was generated by pyright.
"""

from typing import Optional
from openbb_terminal.decorators import log_start_end

""" ECB view """
__docformat__ = ...
logger = ...
ID_TO_NAME = ...
ESTR_PARAMETER_TO_ECB_ID = ...
@log_start_end(log=logger)
def plot_estr(parameter: str = ..., start_date: Optional[str] = ..., end_date: Optional[str] = ..., export: str = ..., sheet_name: str = ..., external_axes: bool = ...): # -> OpenBBFigure | None:
    """Plot Euro Short-Term Rate (ESTR)

    Parameters
    ----------
    series_id: str
        ECB ID of ESTR data to plot, options: ['EST.B.EU000A2X2A25.WT', 'EST.B.EU000A2X2A25.TT',
        'EST.B.EU000A2X2A25.NT', 'EST.B.EU000A2X2A25.R75', 'EST.B.EU000A2X2A25.NB',
        'EST.B.EU000A2X2A25.VL', 'EST.B.EU000A2X2A25.R25']
    start_date: Optional[str]
        Start date, formatted YYYY-MM-DD
    end_date: Optional[str]
        End date, formatted YYYY-MM-DD
    export: str
        Export data to csv or excel file
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    ...

@log_start_end(log=logger)
def display_ecb_yield_curve(date: str = ..., yield_type: str = ..., detailed: bool = ..., any_rating: bool = ..., external_axes: bool = ..., raw: bool = ..., export: str = ..., sheet_name: str = ...): # -> OpenBBFigure | None:
    """Display yield curve based on ECB Treasury rates for a specified date.

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
        Date to get curve for. If None, gets most recent date (format yyyy-mm-dd)
    yield_type: str
        What type of yield curve to get, options: ['spot_rate', 'instantaneous_forward', 'par_yield']
    detailed: bool
        If True, returns detailed data. Note that this is very slow.
    aaa_only: bool
        If True, it only returns rates for AAA rated bonds. If False, it returns rates for all bonds
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    raw : bool
        Output only raw data
    export : str
        Export data to csv,json,xlsx or png,jpg,pdf,svg file
    """
    ...

