"""
This type stub file was generated by pyright.
"""

import argparse
import matplotlib.pyplot as plt
import pandas as pd
import requests
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from openbb_terminal import OpenBBFigure
from openbb_terminal.core.session.current_user import get_current_user
from openbb_terminal.decorators import check_api_key

"""Helper functions."""
__docformat__ = ...
logger = ...
if (get_current_user().preferences.PLOT_BACKEND is not None and get_current_user().preferences.PLOT_BACKEND != "None"):
    ...
NO_EXPORT = ...
EXPORT_ONLY_RAW_DATA_ALLOWED = ...
EXPORT_ONLY_FIGURES_ALLOWED = ...
EXPORT_BOTH_RAW_DATA_AND_FIGURES = ...
MENU_GO_BACK = ...
MENU_QUIT = ...
MENU_RESET = ...
GPT_INDEX_DIRECTORY = ...
GPT_INDEX_VER = ...
command_location = ...
def set_command_location(cmd_loc: str): # -> None:
    """Set command location.

    Parameters
    ----------
    cmd_loc: str
        Command location called by user
    """
    ...

def check_path(path: str) -> str:
    """Check that path file exists.

    Parameters
    ----------
    path: str
        path of file

    Returns
    -------
    str:
        Ratio of similarity between two strings
    """
    ...

def parse_and_split_input(an_input: str, custom_filters: List) -> List[str]:
    """Filter and split the input queue.

    Uses regex to filters command arguments that have forward slashes so that it doesn't
    break the execution of the command queue.
    Currently handles unix paths and sorting settings for screener menus.

    Parameters
    ----------
    an_input : str
        User input as string
    custom_filters : List
        Additional regular expressions to match

    Returns
    -------
    List[str]
        Command queue as list
    """
    ...

def log_and_raise(error: Union[argparse.ArgumentTypeError, ValueError]) -> None:
    """Log and output an error."""
    ...

def similar(a: str, b: str) -> float:
    """Return a similarity float between string a and string b.

    Parameters
    ----------
    a: str
        string a
    b: str
        string b

    Returns
    -------
    float:
        Ratio of similarity between two strings
    """
    ...

def return_colored_value(value: str): # -> str:
    """Return the string value with green, yellow, red or white color based on
    whether the number is positive, negative, zero or other, respectively.

    Parameters
    ----------
    value: str
        string to be checked

    Returns
    -------
    value: str
        string with color based on value of number if it exists
    """
    ...

def print_rich_table(df: pd.DataFrame, show_index: bool = ..., title: str = ..., index_name: str = ..., headers: Optional[Union[List[str], pd.Index]] = ..., floatfmt: Union[str, List[str]] = ..., show_header: bool = ..., automatic_coloring: bool = ..., columns_to_auto_color: Optional[List[str]] = ..., rows_to_auto_color: Optional[List[str]] = ..., export: bool = ..., print_to_console: bool = ..., limit: Optional[int] = ..., source: Optional[str] = ..., columns_keep_types: Optional[List[str]] = ...): # -> None:
    """Prepare a table from df in rich.

    Parameters
    ----------
    df: pd.DataFrame
        Dataframe to turn into table
    show_index: bool
        Whether to include index
    title: str
        Title for table
    index_name : str
        Title for index column
    headers: List[str]
        Titles for columns
    floatfmt: Union[str, List[str]]
        Float number formatting specs as string or list of strings. Defaults to ".2f"
    show_header: bool
        Whether to show the header row.
    automatic_coloring: bool
        Automatically color a table based on positive and negative values
    columns_to_auto_color: List[str]
        Columns to automatically color
    rows_to_auto_color: List[str]
        Rows to automatically color
    export: bool
        Whether we are exporting the table to a file. If so, we don't want to print it.
    limit: Optional[int]
        Limit the number of rows to show.
    print_to_console: bool
        Whether to print the table to the console. If False and interactive mode is
        enabled, the table will be displayed in a new window. Otherwise, it will print to the
        console.
    source: Optional[str]
        Source of the table. If provided, it will be displayed in the header of the table.
    columns_keep_types: Optional[List[str]]
        Columns to keep their types, i.e. not convert to numeric
    """
    ...

def check_int_range(mini: int, maxi: int): # -> (num: int) -> int:
    """Check if argparse argument is an int between 2 values.

    Parameters
    ----------
    mini: int
        Min value to compare
    maxi: int
        Max value to compare

    Returns
    -------
    int_range_checker:
        Function that compares the three integers
    """
    ...

def check_non_negative(value) -> int:
    """Argparse type to check non negative int."""
    ...

def check_terra_address_format(address: str) -> str:
    """Validate that terra account address has proper format.

    Example: ^terra1[a-z0-9]{38}$

    Parameters
    ----------
    address: str
        terra blockchain account address
    Returns
    -------
    str
        Terra blockchain address or raise argparse exception
    """
    ...

def check_non_negative_float(value) -> float:
    """Argparse type to check non negative int."""
    ...

def check_positive_list(value) -> List[int]:
    """Argparse type to return list of positive ints."""
    ...

def check_positive(value) -> int:
    """Argparse type to check positive int."""
    ...

def check_indicators(string: str) -> List[str]:
    """Check if indicators are valid."""
    ...

def check_indicator_parameters(args: str, _help: bool = ...) -> str:
    """Check if indicators parameters are valid."""
    ...

def check_positive_float(value) -> float:
    """Argparse type to check positive float."""
    ...

def check_percentage_range(num) -> float:
    """Check if float is between 0 and 100. If so, return it.

    Parameters
    ----------
    num: float
        Input float

    Returns
    -------
    num: float
        Input number if conditions are met

    Raises
    ------
    argparse.ArgumentTypeError
        Input number not between min and max values
    """
    ...

def check_proportion_range(num) -> float:
    """Check if float is between 0 and 1. If so, return it.

    Parameters
    ----------
    num: float
        Input float
    Returns
    -------
    num: float
        Input number if conditions are met
    Raises
    ----------
    argparse.ArgumentTypeError
        Input number not between min and max values
    """
    ...

def valid_date_in_past(s: str) -> datetime:
    """Argparse type to check date is in valid format."""
    ...

def check_list_dates(str_dates: str) -> List[datetime]:
    """Argparse type to check list of dates provided have a valid format.

    Parameters
    ----------
    str_dates: str
        string with dates separated by ","

    Returns
    -------
    list_dates: List[datetime]
        List of valid dates
    """
    ...

def valid_date(s: str) -> datetime:
    """Argparse type to check date is in valid format."""
    ...

def is_valid_date(s: str) -> bool:
    """Check if date is in valid format."""
    ...

def valid_repo(repo: str) -> str:
    """Argparse type to check github repo is in valid format."""
    ...

def valid_hour(hr: str) -> int:
    """Argparse type to check hour is valid with 24-hour notation."""
    ...

def lower_str(string: str) -> str:
    """Convert string to lowercase."""
    ...

def us_market_holidays(years) -> list:
    """Get US market holidays."""
    ...

def lambda_long_number_format(num, round_decimal=...) -> Union[str, int, float]:
    """Format a long number."""
    ...

def revert_lambda_long_number_format(num_str: str) -> Union[float, str]:
    """
    Revert the formatting of a long number if the input is a formatted number, otherwise return the input as is.

    Parameters
    ----------
    num_str : str
        The number to remove the formatting.

    Returns
    -------
    Union[float, str]
        The number as float (with no formatting) or the input as is.

    """
    ...

def lambda_long_number_format_y_axis(df, y_column, ax): # -> None:
    """Format long number that goes onto Y axis."""
    ...

def lambda_clean_data_values_to_float(val: str) -> float:
    """Clean data to float based on string ending."""
    ...

def lambda_int_or_round_float(x) -> str:
    """Format int or round float."""
    ...

def divide_chunks(data, n): # -> Generator[Unknown, Any, None]:
    """Split into chunks."""
    ...

def get_next_stock_market_days(last_stock_day, n_next_days) -> list:
    """Get the next stock market day.

    Checks against weekends and holidays.
    """
    ...

def is_intraday(df: pd.DataFrame) -> bool:
    """Check if the data granularity is intraday.

    Parameters
    ----------
    df : pd.DataFrame
        Price data

    Returns
    -------
    bool
        True if data is intraday
    """
    ...

def reindex_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Reindex dataframe to exclude non-trading days.

    Resets the index of a df to an integer and prepares the 'date' column to become
    x tick labels on a plot.

    Parameters
    ----------
    df : pd.DataFrame
        Source dataframe

    Returns
    -------
    pd.DataFrame
        Reindexed dataframe
    """
    ...

def get_data(tweet): # -> dict[str, Unknown]:
    """Get twitter data from API request."""
    ...

def clean_tweet(tweet: str, symbol: str) -> str:
    """Clean tweets to be fed to sentiment model."""
    ...

def get_user_agent() -> str:
    """Get a not very random user agent."""
    ...

def text_adjustment_init(self): # -> None:
    """Adjust text monkey patch for Pandas."""
    ...

def text_adjustment_len(self, text): # -> int:
    """Get the length of the text adjustment."""
    ...

def text_adjustment_justify(self, texts, max_len, mode=...): # -> list[Unknown]:
    """Apply 'Justify' text alignment."""
    ...

def text_adjustment_join_unicode(self, lines, sep=...): # -> str:
    """Join Unicode."""
    ...

def text_adjustment_adjoin(self, space, *lists, **kwargs):
    """Join text."""
    ...

def patch_pandas_text_adjustment(): # -> None:
    """Set pandas text adjustment settings."""
    ...

def lambda_financials_colored_values(val: str) -> str:
    """Add a color to a value."""
    ...

def check_ohlc(type_ohlc: str) -> str:
    """Check that data is in ohlc."""
    ...

def lett_to_num(word: str) -> str:
    """Match ohlca to integers."""
    ...

AVAILABLE_FLAIRS = ...
def get_flair() -> str:
    """Get a flair icon."""
    ...

def is_timezone_valid(user_tz: str) -> bool:
    """Check whether user timezone is valid.

    Parameters
    ----------
    user_tz: str
        Timezone to check for validity

    Returns
    -------
    bool
        True if timezone provided is valid
    """
    ...

def get_user_timezone() -> str:
    """Get user timezone if it is a valid one.

    Returns
    -------
    str
        user timezone based on .env file
    """
    ...

def get_user_timezone_or_invalid() -> str:
    """Get user timezone if it is a valid one.

    Returns
    -------
    str
        user timezone based on timezone.openbb file or INVALID
    """
    ...

def str_to_bool(value) -> bool:
    """Match a string to a boolean value."""
    ...

def get_screeninfo(): # -> tuple[int, int] | None:
    """Get screeninfo."""
    ...

def plot_autoscale(): # -> tuple[float, float]:
    """Autoscale plot."""
    ...

def get_last_time_market_was_open(dt):
    """Get last time the US market was open."""
    ...

def check_file_type_saved(valid_types: Optional[List[str]] = ...): # -> (filenames: str = "") -> str:
    """Provide valid types for the user to be able to select.

    Parameters
    ----------
    valid_types: List[str]
        List of valid types to export data

    Returns
    -------
    check_filenames: Optional[List[str]]
        Function that returns list of filenames to export data
    """
    ...

def compose_export_path(func_name: str, dir_path: str) -> Path:
    """Compose export path for data from the terminal.

    Creates a path to a folder and a filename based on conditions.

    Parameters
    ----------
    func_name : str
        Name of the command that invokes this function
    dir_path : str
        Path of directory from where this function is called

    Returns
    -------
    Path
        Path variable containing the path of the exported file
    """
    ...

def ask_file_overwrite(file_path: Path) -> Tuple[bool, bool]:
    """Helper to provide a prompt for overwriting existing files.

    Returns two values, the first is a boolean indicating if the file exists and the
    second is a boolean indicating if the user wants to overwrite the file.
    """
    ...

def export_data(export_type: str, dir_path: str, func_name: str, df: pd.DataFrame = ..., sheet_name: Optional[str] = ..., figure: Optional[OpenBBFigure] = ..., margin: bool = ...) -> None:
    """Export data to a file.

    Parameters
    ----------
    export_type : str
        Type of export between: csv,json,xlsx,xls
    dir_path : str
        Path of directory from where this function is called
    func_name : str
        Name of the command that invokes this function
    df : pd.Dataframe
        Dataframe of data to save
    sheet_name : str
        If provided.  The name of the sheet to save in excel file
    figure : Optional[OpenBBFigure]
        Figure object to save as image file
    margin : bool
        Automatically adjust subplot parameters to give specified padding.
    """
    ...

def get_rf() -> float:
    """Use the fiscaldata.gov API to get most recent T-Bill rate.

    Returns
    -------
    rate : float
        The current US T-Bill rate
    """
    ...

def system_clear(): # -> None:
    """Clear screen."""
    ...

def excel_columns() -> List[str]:
    """Return potential columns for excel.

    Returns
    -------
    letters : List[str]
        Letters to be used as excel columns
    """
    ...

def handle_error_code(requests_obj, error_code_map): # -> None:
    """Handle error code of HTTP requests.

    Parameters
    ----------
    requests_obj: Object
        Request object
    error_code_map: Dict
        Dictionary mapping of HTTP error code and output message

    """
    ...

def prefill_form(ticket_type, menu, path, command, message): # -> None:
    """Pre-fill Google Form and open it in the browser."""
    ...

def get_closing_price(ticker, days):
    """Get historical close price for n days in past for market asset.

    Parameters
    ----------
    ticker : str
        Ticker to get data for
    days : datetime
        No. of days in past

    Returns
    -------
    data : pd.DataFrame
        Historic close prices for ticker for given days
    """
    ...

def camel_case_split(string: str) -> str:
    """Convert a camel-case string to separate words.

    Parameters
    ----------
    string : str
        The string to be converted

    Returns
    -------
    new_string: str
        The formatted string
    """
    ...

def is_valid_axes_count(axes: List[plt.Axes], n: int, custom_text: Optional[str] = ..., prefix_text: Optional[str] = ..., suffix_text: Optional[str] = ...): # -> bool:
    """Check if axes list length is equal to n and log text if check result is false.

    Parameters
    ----------
    axes: List[plt.Axes]
        External axes (2 axes are expected in the list)
    n: int
        number of expected axes
    custom_text: Optional[str] = None
        custom text to log
    prefix_text: Optional[str] = None
        prefix text to add before text to log
    suffix_text: Optional[str] = None
        suffix text to add after text to log
    """
    ...

def support_message(s: str) -> str:
    """Argparse type to check string is in valid format for the support command."""
    ...

def check_list_values(valid_values: List[str]): # -> (given_values: str) -> List[str]:
    """Get valid values to test arguments given by user.

    Parameters
    ----------
    valid_values: List[str]
        List of valid values to be checked

    Returns
    -------
    check_list_values_from_valid_values_list:
        Function that ensures that the valid values go through and notifies user when value is not valid.
    """
    ...

def search_wikipedia(expression: str) -> None:
    """Search wikipedia for a given expression.

    Parameters
    ----------
    expression: str
        Expression to search for
    """
    ...

def screenshot() -> None:
    """Screenshot the terminal window or the plot window.

    Parameters
    ----------
    terminal_window_target: bool
        Target the terminal window
    """
    ...

def screenshot_to_canvas(shot, plot_exists: bool = ...): # -> None:
    """Frame image to OpenBB canvas.

    Parameters
    ----------
    shot
        Image to frame with OpenBB Canvas
    plot_exists: bool
        Variable to say whether the image is a plot or screenshot of terminal
    """
    ...

@lru_cache
def load_json(path: Path) -> Dict[str, str]:
    """Load a dictionary from a json file path.

    Parameter
    ----------
    path : Path
        The path for the json file

    Returns
    -------
    Dict[str, str]
        The dictionary loaded from json
    """
    ...

def list_from_str(value: str) -> List[str]:
    """Convert a string to a list.

    Parameter
    ---------
    value : str
        The string to convert

    Returns
    -------
    new_value: List[str]
        The list of strings
    """
    ...

def str_date_to_timestamp(date: str) -> int:
    """Transform string date to timestamp

    Parameters
    ----------
    start_date : str
        Initial date, format YYYY-MM-DD

    Returns
    -------
    date_ts : int
        Initial date timestamp (e.g., 1_614_556_800)
    """
    ...

def check_start_less_than_end(start_date: str, end_date: str) -> bool:
    """Check if start_date is equal to end_date.

    Parameters
    ----------
    start_date : str
        Initial date, format YYYY-MM-DD
    end_date : str
        Final date, format YYYY-MM-DD

    Returns
    -------
    bool
        True if start_date is not equal to end_date, False otherwise
    """
    ...

def request(url: str, method: str = ..., timeout: int = ..., **kwargs) -> requests.Response:
    """Abstract helper to make requests from a url with potential headers and params.

    Parameters
    ----------
    url : str
        Url to make the request to
    method : str, optional
        HTTP method to use.  Can be "GET" or "POST", by default "GET"

    Returns
    -------
    requests.Response
        Request response object

    Raises
    ------
    ValueError
        If invalid method is passed
    """
    ...

def remove_timezone_from_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove timezone information from a dataframe.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe to remove timezone information from

    Returns
    -------
    pd.DataFrame
        The dataframe with timezone information removed
    """
    ...

@check_api_key(["API_OPENAI_KEY"])
def query_LLM_local(query_text, gpt_model): # -> tuple[str | Unknown | None, List[NodeWithScore]] | tuple[None, None] | None:
    ...

def query_LLM_remote(query_text: str): # -> tuple[None, None] | tuple[Any, Any]:
    """Query askobb on gpt-3.5 turbo hosted model

    Parameters
    ----------
    query_text : str
        Query string for askobb
    """
    ...

