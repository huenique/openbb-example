"""
This type stub file was generated by pyright.
"""

from openbb_terminal.core.sdk.sdk_helpers import Category

class QaRoot(Category):
    """Quantitative Analysis Module

    Attributes:
        `acf`: Plots Auto and Partial Auto Correlation of returns and change in returns\n
        `bw`: Plots box and whisker plots\n
        `calculate_adjusted_var`: Calculates VaR, which is adjusted for skew and kurtosis (Cornish-Fischer-Expansion)\n
        `cdf`: Plots Cumulative Distribution Function\n
        `cusum`: Plots Cumulative sum algorithm (CUSUM) to detect abrupt changes in data\n
        `decompose`: Perform seasonal decomposition\n
        `es`: Gets Expected Shortfall for specified stock dataframe.\n
        `es_chart`: Prints table showing expected shortfall.\n
        `hist`: Plots histogram of data\n
        `kurtosis`: Kurtosis Indicator\n
        `kurtosis_chart`: Plots rolling kurtosis\n
        `line`: Display line plot of data\n
        `normality`: Look at the distribution of returns and generate statistics on the relation to the normal curve.\n
        `normality_chart`: Prints table showing normality statistics\n
        `omega`: Get the omega series\n
        `omega_chart`: Plots the omega ratio\n
        `qqplot`: Plots QQ plot for data against normal quantiles\n
        `quantile`: Overlay Median & Quantile\n
        `quantile_chart`: Plots rolling quantile\n
        `rolling`: Return rolling mean and standard deviation\n
        `rolling_chart`: Plots mean std deviation\n
        `sharpe`: Calculates the sharpe ratio\n
        `sharpe_chart`: Plots Calculated the sharpe ratio\n
        `skew`: Skewness Indicator\n
        `skew_chart`: Plots rolling skew\n
        `sortino`: Calculates the sortino ratio\n
        `sortino_chart`: Plots the sortino ratio\n
        `spread`: Standard Deviation and Variance\n
        `spread_chart`: Plots rolling spread\n
        `summary`: Print summary statistics\n
        `summary_chart`: Prints table showing summary statistics\n
        `unitroot`: Calculate test statistics for unit roots\n
        `unitroot_chart`: Prints table showing unit root test calculations\n
        `var`: Gets value at risk for specified stock dataframe.\n
        `var_chart`: Prints table showing VaR of dataframe.\n
    """
    _location_path = ...
    def __init__(self) -> None:
        ...
    


