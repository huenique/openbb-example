"""
This type stub file was generated by pyright.
"""

from openbb_terminal.core.sdk.sdk_helpers import Category

class EtfRoot(Category):
    """Etf Module

    Attributes:
        `candle`: Show candle plot of loaded ticker.\n
        `compare`: Compare selected ETFs\n
        `etf_by_category`: Return a selection of ETFs based on category filtered by total assets.\n
        `etf_by_name`: Get an ETF symbol and name based on ETF string to search. [Source: StockAnalysis]\n
        `holdings`: Get ETF holdings\n
        `ld`: Return a selection of ETFs based on description filtered by total assets.\n
        `ln`: Return a selection of ETFs based on name filtered by total assets. [Source: Finance Database]\n
        `load`: Load a symbol to perform analysis using the string above as a template.\n
        `news`: Get news for a given term. [Source: NewsAPI]\n
        `news_chart`: Prints table showing news for a given term. [Source: NewsAPI]\n
        `overview`: Get overview data for selected etf\n
        `symbols`: Gets all etf names and symbols\n
        `weights`: Return sector weightings allocation of ETF. [Source: FinancialModelingPrep]\n
    """
    _location_path = ...
    def __init__(self) -> None:
        ...
    


class EtfDiscovery(Category):
    """Discovery Module.

    Attributes:
        `mover`: Scrape data for top etf movers.\n
    """
    _location_path = ...
    def __init__(self) -> None:
        ...
    

