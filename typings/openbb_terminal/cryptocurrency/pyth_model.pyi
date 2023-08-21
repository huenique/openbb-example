"""
This type stub file was generated by pyright.
"""

from typing import Tuple

logger = ...
ASSETS = ...
async def get_price(symbol: str) -> Tuple[float, float, float]:
    """Returns price and confidence interval from pyth live feed. [Source: Pyth]

    Parameters
    ----------
    symbol : str
        Symbol of the asset to get price and confidence interval from

    Returns
    -------
    Tuple[float, float, float]
        Price of the asset,
        Confidence level,
        Previous price of the asset
    """
    ...

