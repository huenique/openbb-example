"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Any, List, Optional

PLT_3DMESH_COLORSCALE = ...
PLT_3DMESH_SCENE = ...
PLT_3DMESH_HOVERLABEL = ...
PLT_STYLE_TEMPLATE = ...
PLT_STYLE_INCREASING = ...
PLT_STYLE_DECREASING = ...
PLT_CANDLESTICKS = ...
PLT_STYLE_INCREASING_GREEN = ...
PLT_STYLE_DECREASING_RED = ...
PLT_FONT = ...
PLOTLY_FONT = ...
PLT_COLORWAY = ...
PLT_FIB_COLORWAY: List[Any] = ...
PLT_INCREASING_COLORWAY = ...
PLT_DECREASING_COLORWAY = ...
PLT_INCREASING_COLORWAY_GREEN = ...
PLT_DECREASING_COLORWAY_RED = ...
PLT_TBL_HEADER = ...
PLT_TBL_CELLS = ...
PLT_TBL_ROW_COLORS = ...
def de_increasing_color_list(df_column: Optional[pd.DataFrame] = ..., text: Optional[str] = ..., contains_str: str = ..., increasing_color: str = ..., decreasing_color: str = ...) -> List[str]:
    """Makes a colorlist for decrease/increase if value in df_column
    contains "{contains_str}" default is "-"

    Parameters
    ----------
    df_column : pd.DataFrame, optional
        Dataframe column to create colorlist. by default None
    text : str, optional
        Search in a string, by default None
    contains_str : str, optional
        Decreasing String to search for in df_column. The default is "-".
    increasing_color : str, optional
        Color to use for increasing values. The default is PLT_STYLE_INCREASING.
    decreasing_color : str, optional
        Color to use for decreasing values. The default is PLT_STYLE_DECREASING.

    Returns
    -------
    List[str]
        List of colors for df_column
    """
    ...

PLOTLY_THEME = ...