"""
This type stub file was generated by pyright.
"""

import pandas as pd
from openbb_terminal.decorators import log_start_end

""" opensea.io Model """
logger = ...
API_URL = ...
@log_start_end(log=logger)
def get_collection_stats(slug: str) -> pd.DataFrame:
    """Get stats of a nft collection [Source: opensea.io]

    Parameters
    ----------
    slug : str
        Opensea collection slug. If the name of the collection is Mutant Ape Yacht Club the slug is mutant-ape-yacht-club

    Returns
    -------
    pd.DataFrame
        collection stats
    """
    ...
