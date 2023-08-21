"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Callable, Dict, Literal, Optional, Tuple
from pandas._typing import Axis

"""Denomination Helper functions"""
DENOMINATION = Literal["Trillions", "Billions", "Millions", "Tens of thousands", "Thousands", "Units", ""]
def transform(df: pd.DataFrame, sourceDenomination: DENOMINATION = ..., targetDenomination: Optional[DENOMINATION] = ..., maxValue: Optional[float] = ..., axis: Axis = ..., skipPredicate: Optional[Callable[[pd.Series], bool]] = ...) -> Tuple[pd.DataFrame, DENOMINATION]:
    """Transforms data frame by denomination.

    Args:
        df (pd.DataFrame): Source data frame
        sourceDenomination (DENOMINATION, optional): Current denomination. Defaults to Units.
        targetDenomination (DENOMINATION, optional): Desired denomination. Defaults to None, meaning we will find it.
        maxValue (float, optional): Max value of the data frame. Defaults to None, meaning df.max().max() will be used.
        axis (Axis, optional): Axis to apply to skip predicate. Defaults to 0.
        skipPredicate (Callable[[pd.Series], bool], optional): Predicate for skipping a transform.
    Returns:
    pd.DataFrame
        Tuple[pd.DataFrame, DENOMINATION]: Pair of transformed data frame and applied denomination.
    """
    ...

def get_denominations() -> Dict[DENOMINATION, float]:
    """Gets all supported denominations and their lower bound value

    Returns:
        Dict[DENOMINATION, int]: All supported denominations and their lower bound value
    """
    ...

def get_denomination(value: float) -> Tuple[DENOMINATION, float]:
    """Gets denomination that fits the supplied value.
       If no denomination found, 'Units' is returned.

    Args:
        value (int): Value

    Returns:
        Tuple[DENOMINATION, int]:Denomination that fits the supplied value
    """
    ...
