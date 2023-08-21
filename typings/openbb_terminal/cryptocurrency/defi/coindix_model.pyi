"""
This type stub file was generated by pyright.
"""

import pandas as pd
from typing import Optional
from openbb_terminal.decorators import log_start_end

"""Coindix model"""
__docformat__ = ...
logger = ...
VAULTS_FILTERS = ...
CHAINS = ...
PROTOCOLS = ...
VAULT_KINDS = ...
@log_start_end(log=logger)
def get_defi_vaults(chain: Optional[str] = ..., protocol: Optional[str] = ..., kind: Optional[str] = ..., ascend: bool = ..., sortby: str = ...) -> pd.DataFrame:
    """Get DeFi Vaults Information. DeFi Vaults are pools of funds with an assigned strategy which main goal is to
    maximize returns of its crypto assets. [Source: https://coindix.com/]

    Parameters
    ----------
    chain: str
        Blockchain - one from list [
        'ethereum', 'polygon', 'avalanche', 'bsc', 'terra', 'fantom',
        'moonriver', 'celo', 'heco', 'okex', 'cronos', 'arbitrum', 'eth',
        'harmony', 'fuse', 'defichain', 'solana', 'optimism'
        ]
    protocol: str
        DeFi protocol - one from list: [
        'aave', 'acryptos', 'alpaca', 'anchor', 'autofarm', 'balancer', 'bancor',
        'beefy', 'belt', 'compound', 'convex', 'cream', 'curve', 'defichain', 'geist',
        'lido', 'liquity', 'mirror', 'pancakeswap', 'raydium', 'sushi', 'tarot', 'traderjoe',
        'tulip', 'ubeswap', 'uniswap', 'venus', 'yearn'
        ]
    kind: str
        Kind/type of vault - one from list: ['lp','single','noimploss','stable']

    Returns
    -------
    pd.DataFrame
        Top 100 DeFi Vaults for given chain/protocol sorted by APY.
    """
    ...

