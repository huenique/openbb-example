"""
This type stub file was generated by pyright.
"""

from pathlib import Path
from typing import Any, Dict, List, Union
from openbb_terminal.decorators import log_start_end

"""Reports Model Module."""
__docformat__ = ...
logger = ...
CURRENT_LOCATION = ...
REPORTS_FOLDER = ...
USER_REPORTS = ...
etf_data_path = ...
ETF_TICKERS = ...
crypto_data_path = ...
CRYPTO_TICKERS = ...
stocks_data_path = ...
STOCKS_TICKERS = ...
PORTFOLIO_HOLDINGS_FILES = ...
REPORT_CHOICES = ...
TARGET_TAG = ...
@log_start_end(log=logger)
def get_arg_choices(report_name: str, arg_name: str) -> Union[List[str], None]:
    """Get argument choices from autocompletion for crypto, forex and portfolio.

    Parameters
    ----------
    report_name: str
        Name of report chosen.
    arg_name: str
        Argument to limit choices.

    Returns:
        List[str]: List with argument choices from autocompletion.
    """
    ...

@log_start_end(log=logger)
def get_reports_available(folder: Path = ..., warn: bool = ...) -> List[str]:
    """Get Jupyter notebook available in folder.

    Parameters
    ----------
    folder: Path
        Path to folder.

    Returns:
        List[str]: List with names of notebooks available.
    """
    ...

@log_start_end(log=logger)
def extract_parameters(input_path: str) -> Dict[str, str]:
    """Extract required parameters from notebook content.

    Parameters
    ----------
    input_path: str
        Path of report to be rendered.

    Returns:
        Dict[str, str]: Dictionary with parameters names and values.
    """
    ...

@log_start_end(log=logger)
def render_report(input_path: str, args_dict: Dict[str, str]): # -> None:
    """Report rendering end to end.

    Workflow:
        1. Update parameters to use in notebook with received arguments
        2. Create output path
        3. Update parameters with output_path
        4. Validate and execute notebook in a new thread.

    Parameters
    ----------
    input_path: str
        Path of report to be rendered.
    args_dict: Dict[str, str]
        Dictionary with received arguments dictionary.
    """
    ...

@log_start_end(log=logger)
def update_parameters(input_path: str, args_dict: Dict[str, str]) -> Dict[str, Any]:
    """Update dictionary of parameters to be used in report with received arguments.

    Parameters
    ----------
    input_path: str
        Path of report to be rendered.
    args_dict: Dict[str, str]
        Dictionary with received arguments dictionary.

    Returns
    -------
    Dict[str, Any]
        Dictionary with report parameters.
    """
    ...

@log_start_end(log=logger)
def create_output_path(input_path: str, parameters_dict: Dict[str, Any]) -> str:
    """Create path to save rendered report, thus the output path.

    Parameters
    ----------
    input_path: str
        Path of report to be rendered.
    parameters_dict: Dict[str, Any]
        Dictionary with report parameters.

    Returns
    -------
    str
        Path of rendered report.
    """
    ...

@log_start_end(log=logger)
def execute_notebook(input_path, parameters, output_path): # -> None:
    """Execute the input path's notebook with the parameters provided.
    Then, save it in the output path.

    Parameters
    ----------
    input_path: str
        Path of report to be rendered.
    parameters: Dict[str, Any]
        Dictionary with report parameters.
    output_path: str
        Path of rendered report.
    """
    ...

@log_start_end(log=logger)
def add_ipynb_extension(path: str) -> str:
    """Add .ipynb extension to path.
    Parameters
    ----------
    path: str
        Path to notebook file.

    Returns
    -------
    str
        Path to .ipynb file.
    """
    ...

@log_start_end(log=logger)
def check_ipynb(path: str) -> str:
    """Check if there is .ipynb extension in path.
    This is useful to the controller type check.

    Parameters
    ----------
    path: str
        Path to notebook file.

    Returns
    -------
    bool
        Path if paths endswith .ipynb, else empty string.
    """
    ...

def ipykernel_launcher(module_file: str, module_hist_file: str): # -> None:
    """This function mocks 'ipykernel_launcher.py' launching a Jupyter notebook kernel.

    It is useful when running python commands inside a frozen application like our
    installer distribution, where sys.executable[0] is not the path to python
    interpreter, rather it is the path to the application executable.

    Problem:
        'papermill' was trying to execute the following command on a subprocess:
        $ .../bin/python -m ipykernel_launcher -f ... --HistoryManager.hist_file ...

        'papermill' was using '.../bin/python' because it is looks for the sys.executable[0],
        which most of the time leads to the python interpreter. In our frozen app,
        sys.executable[0] leads to 'OpenBB Terminal/.OpenBB/OpenBBTerminal', which in turn
        executes 'terminal.py.

        This means that the command was being executed in 'terminal.py'. Consequently,
        one gets the following error message:
        $ terminal: error: unrecognized arguments: -m ipykernel_launcher -f ... --HistoryManager.hist_file ...

    Solution:
        Parse 'papermill' command in the 'terminal_controller', which is what follows
        'terminal.py' and here receive the parsed 'papermill' command arguments and
        route them to IPKernelApp as if this is 'ipykernel_launcher' module
        - the kernel is launched.

    Source: https://pyinstaller.org/en/stable/runtime-information.html#using-sys-executable-and-sys-argv-0

    Parameters
    ----------
    module_file: str
        Specified connection file.
    module_hist_file: str
        History manager file.
    """
    ...
