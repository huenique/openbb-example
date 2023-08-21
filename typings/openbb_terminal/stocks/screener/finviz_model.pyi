"""
This type stub file was generated by pyright.
"""

from openbb_terminal.decorators import log_start_end

logger = ...
PRESETS_PATH = ...
PRESETS_PATH_DEFAULT = ...
preset_choices = ...
if PRESETS_PATH.exists():
    ...
if PRESETS_PATH_DEFAULT.exists():
    ...
d_signals = ...
@log_start_end(log=logger)
def get_screener_data(preset_loaded: str = ..., data_type: str = ..., limit: int = ..., ascend: bool = ...): # -> DataFrame | None:
    """Screener Overview

    Parameters
    ----------
    preset_loaded : str
        Loaded preset filter
    data_type : str
        Data type between: overview, valuation, financial, ownership, performance, technical
    limit : int
        Limit of stocks filtered with presets to print
    ascend : bool
        Ascended order of stocks filtered to print

    Returns
    -------
    pd.DataFrame
        Dataframe with loaded filtered stocks
    """
    ...

d_signals_desc = ...
d_check_screener = ...
