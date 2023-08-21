"""
This type stub file was generated by pyright.
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, TYPE_CHECKING, TypeVar, Union

"""Chart and style helpers for Plotly."""
if TYPE_CHECKING:
    ...
TimeSeriesT = TypeVar("TimeSeriesT", bound="TimeSeries")
class TerminalStyle:
    """The class that helps with handling of style configurations.

    It serves styles for 2 libraries. For `Plotly` this class serves absolute paths
    to the .pltstyle files. For `Plotly` and `Rich` this class serves custom
    styles as python dictionaries.
    """
    STYLES_REPO = ...
    USER_STYLES_DIRECTORY = ...
    plt_styles_available: Dict[str, Path] = ...
    plt_style: str = ...
    plotly_template: Dict[str, Any] = ...
    mapbox_style: str = ...
    console_styles_available: Dict[str, Path] = ...
    console_style: Dict[str, Any] = ...
    line_color: str = ...
    up_color: str = ...
    down_color: str = ...
    up_colorway: List[str] = ...
    down_colorway: List[str] = ...
    up_color_transparent: str = ...
    down_color_transparent: str = ...
    line_width: float = ...
    def __new__(cls, *args, **kwargs): # -> Self@TerminalStyle:
        """Create a singleton."""
        ...
    
    def __init__(self, plt_style: Optional[str] = ..., console_style: Optional[str] = ...) -> None:
        """Initialize the class.

        Parameters
        ----------
        plt_style : `str`, optional
            The name of the Plotly style to use, by default ""
        console_style : `str`, optional
            The name of the Rich style to use, by default ""
        """
        ...
    
    def apply_console_style(self, style: Optional[str] = ...) -> None:
        """Apply the style to the console."""
        ...
    
    def apply_style(self, style: Optional[str] = ...) -> None:
        """Apply the style to the libraries."""
        ...
    
    def load_available_styles_from_folder(self, folder: Path) -> None:
        """Load custom styles from folder.

        Parses the styles/default and styles/user folders and loads style files.
        To be recognized files need to follow a naming convention:
        *.pltstyle        - plotly stylesheets
        *.richstyle.json  - rich stylesheets

        Parameters
        ----------
        folder : str
            Path to the folder containing the stylesheets
        """
        ...
    
    def load_available_styles(self) -> None:
        """Load custom styles from default and user folders."""
        ...
    
    def load_json_style(self, file: Path) -> Dict[str, Any]:
        """Load style from json file.

        Parameters
        ----------
        file : Path
            Path to the file containing the style

        Returns
        -------
        Dict[str, Any]
            Style as a dictionary
        """
        ...
    
    def load_style(self, style: Optional[str] = ...) -> None:
        """Load style from file.

        Parameters
        ----------
        style : str
            Name of the style to load
        """
        ...
    
    def load_plt_style(self, style: str) -> None:
        """Load Plotly style from file.

        Parameters
        ----------
        style : str
            Name of the style to load
        """
        ...
    
    def get_colors(self, reverse: bool = ...) -> list:
        """Get colors for the plot.

        Parameters
        ----------
        reverse : bool, optional
            Whether to reverse the colors, by default False

        Returns
        -------
        list
            List of colors e.g. ["#00ACFF", "#FF0000"]
        """
        ...
    


theme = ...
class OpenBBFigure(go.Figure):
    """Custom Figure class for OpenBB Terminal.

    Parameters
    ----------
    fig : `go.Figure`, optional
        Figure to copy, by default None
    has_subplots : `bool`, optional
        Whether the figure has subplots, by default False
    **kwargs
        Keyword arguments to pass to `go.Figure.update_layout`

    Class Methods
    -------------
    create_subplots(rows: `int`, cols: `int`, **kwargs) -> `OpenBBFigure`
        Creates a subplots figure
    to_table(data: `pd.DataFrame`, columnwidth: `list`, print_index: `bool`, ...)
        Converts a DataFrame to a table figure

    Methods
    -------
    add_hline_legend(y: `float`, name: `str`, line: `dict`, legendrank: `int`, **kwargs)
        Adds a horizontal line with a legend label
    add_vline_legend(x: `float`, name: `str`, line: `dict`, legendrank: `int`, **kwargs)
        Adds a vertical line with a legend label
    add_legend_label(trace: `str`, label: `str`, mode: `str`, marker: `dict`, **kwargs)
        Adds a legend label
    add_histplot(x: `list`, name: `str`, colors: `list`, bins: `int`, show_curve: `str`, ...)
        Adds a histogram plot
    horizontal_legend(x: `float`, y: `float`, xanchor: `str`, yanchor: `str`, ...)
        Moves the legend to a horizontal position
    to_subplot(subplot: `OpenBBFigure`, row: `int`, col: `int`, secondary_y: `bool`, ...)
        Returns the figure as a subplot of another figure
    """
    plotlyjs_path: Path = ...
    def __init__(self, fig: Optional[go.Figure] = ..., **kwargs) -> None:
        ...
    
    def set_secondary_axis(self, title: str, row: Optional[int] = ..., col: Optional[int] = ..., **kwargs) -> OpenBBFigure:
        """Set secondary axis.

        Parameters
        ----------
        title : str
            Title of the axis
        row : int, optional
            Row of the axis, by default None
        col : int, optional
            Column of the axis, by default None
        **kwargs
            Keyword arguments to pass to go.Figure.update_layout
        """
        ...
    
    @property
    def subplots_kwargs(self): # -> Dict[str, Any]:
        """Get subplots kwargs property."""
        ...
    
    @subplots_kwargs.setter
    def subplots_kwargs(self, value): # -> None:
        """Get subplots kwargs setter."""
        ...
    
    @property
    def has_subplots(self):
        """Has subplots property."""
        ...
    
    @property
    def bar_width(self): # -> float:
        """Bar width property."""
        ...
    
    @bar_width.setter
    def bar_width(self, value): # -> None:
        """Bar width setter."""
        ...
    
    @property
    def cmd_xshift(self): # -> int:
        """Command line x shift property."""
        ...
    
    @cmd_xshift.setter
    def cmd_xshift(self, value): # -> None:
        """Command line x shift setter."""
        ...
    
    @classmethod
    def create_subplots(cls, rows: int = ..., cols: int = ..., shared_xaxes: bool = ..., vertical_spacing: Optional[float] = ..., horizontal_spacing: Optional[float] = ..., subplot_titles: Optional[Union[List[str], tuple]] = ..., row_width: Optional[List[Union[float, int]]] = ..., specs: Optional[List[List[Optional[Dict[Any, Any]]]]] = ..., **kwargs) -> OpenBBFigure:
        """Create a new Plotly figure with subplots.

        Parameters
        ----------
        rows : `int`, optional
            Number of rows, by default 1
        cols : `int`, optional
            Number of columns, by default 1
        shared_xaxes : `bool`, optional
            Whether to share x axes, by default True
        vertical_spacing : `float`, optional
            Vertical spacing between subplots, by default None
        horizontal_spacing : `float`, optional
            Horizontal spacing between subplots, by default None
        subplot_titles : `Union[List[str], tuple]`, optional
            Titles for each subplot, by default None
        row_width : `List[Union[float, int]]`, optional
            Width of each row, by default [1]
        specs : `List[List[dict]]`, optional
            Subplot specs, by default `[[{}] * cols] * rows` (all subplots are the same size)
        """
        ...
    
    def add_trend(self, data: pd.DataFrame, row: int = ..., col: int = ..., secondary_y: bool = ..., **kwargs): # -> None:
        """Add a trend line to the figure.

        Parameters
        ----------
        data : `pd.DataFrame`
            Data to plot
        row : `int`, optional
            Row number, by default 1
        col : `int`, optional
            Column number, by default 1
        secondary_y : `bool`, optional
            Whether to plot on secondary y axis, by default None
        """
        ...
    
    def add_histplot(self, dataset: Union[np.ndarray, pd.Series, TimeSeriesT], name: Optional[Union[str, List[str]]] = ..., colors: Optional[List[str]] = ..., bins: Union[int, str] = ..., curve: Literal["normal", "kde"] = ..., show_curve: bool = ..., show_rug: bool = ..., show_hist: bool = ..., forecast: bool = ..., row: int = ..., col: int = ...) -> None:
        """Add a histogram with a curve and rug plot if desired.

        Parameters
        ----------
        dataset : `Union[np.ndarray, pd.Series, TimeSeriesT]`
            Data to plot
        name : `Optional[Union[str, List[str]]]`, optional
            Name of the plot, by default None
        colors : `Optional[List[str]]`, optional
            Colors of the plot, by default None
        bins : `Union[int, str]`, optional
            Number of bins, by default 15
        curve : `Literal["normal", "kde"]`, optional
            Type of curve to plot, by default "normal"
        show_curve : `bool`, optional
            Whether to show the curve, by default True
        show_rug : `bool`, optional
            Whether to show the rug plot, by default True
        show_hist : `bool`, optional
            Whether to show the histogram, by default True
        forecast : `bool`, optional
            Whether the data is a darts forecast TimeSeries, by default False
        row : `int`, optional
            Row of the subplot, by default 1
        col : `int`, optional
            Column of the subplot, by default 1
        """
        ...
    
    def is_image_export(self, export: Optional[str] = ...) -> bool:
        """Check if the export format is an image format.

        Parameters
        ----------
        export : `str`
            Export format

        Returns
        -------
        `bool`
            True if the export format is an image format, False otherwise
        """
        ...
    
    def set_title(self, title: str, wrap: bool = ..., wrap_width: int = ..., **kwargs) -> OpenBBFigure:
        """Set the main title of the figure.

        Parameters
        ----------
        title : `str`
            Title of the figure
        wrap : `bool`
            If True, the title will be wrapped according to the wrap_width parameter
        wrap_width : `int`
            Width in characters to wrap the title if wrap is True, default is 80
        """
        ...
    
    def set_xaxis_title(self, title: str, row: Optional[int] = ..., col: Optional[int] = ..., **kwargs) -> OpenBBFigure:
        """Set the x axis title of the figure or subplot (if row and col are specified).

        Parameters
        ----------
        title : `str`
            Title of the x axis
        row : `int`, optional
            Row number, by default None
        col : `int`, optional
            Column number, by default None
        """
        ...
    
    def set_yaxis_title(self, title: str, row: Optional[int] = ..., col: Optional[int] = ..., **kwargs) -> OpenBBFigure:
        """Set the y axis title of the figure or subplot (if row and col are specified).

        Parameters
        ----------
        title : `str`
            Title of the x axis
        row : `int`, optional
            Row number, by default None
        col : `int`, optional
            Column number, by default None
        """
        ...
    
    def add_hline_legend(self, y: float, name: str, line: Optional[dict] = ..., legendrank: Optional[int] = ..., **kwargs) -> None:
        """Add a horizontal line with a legend label.

        Parameters
        ----------
        y : `float`
            y value of the line
        name : `str`
            Name of the to display in the legend
        line : `dict`
            Line style
        legendrank : `int`, optional
            Legend rank, by default None (e.g. 1 is above 2)
        """
        ...
    
    def add_vline_legend(self, x: float, name: str, line: Optional[dict] = ..., legendrank: Optional[int] = ..., **kwargs) -> None:
        """Add a vertical line with a legend label.

        Parameters
        ----------
        x : `float`
            x value of the line
        name : `str`
            Name of the to display in the legend
        line : `dict`
            Line style
        legendrank : `int`, optional
            Legend rank, by default None (e.g. 1 is above 2)
        """
        ...
    
    def horizontal_legend(self, x: float = ..., y: float = ..., xanchor: str = ..., yanchor: str = ..., orientation: str = ..., **kwargs) -> None:
        """Set the legend to be horizontal.

        Parameters
        ----------
        x : `float`, optional
            The x position of the legend, by default 1
        y : `float`, optional
            The y position of the legend, by default 1.02
        xanchor : `str`, optional
            The x anchor of the legend, by default "right"
        yanchor : `str`, optional
            The y anchor of the legend, by default "bottom"
        orientation : `str`, optional
            The orientation of the legend, by default "h"
        """
        ...
    
    @staticmethod
    def chart_volume_scaling(df_volume: pd.DataFrame, volume_ticks_x: int = ...) -> Dict[str, list]:
        """Takes df_volume and returns volume_ticks, tickvals for chart volume scaling

        Parameters
        ----------
        df_volume : pd.DataFrame
            Dataframe of volume (e.g. df_volume = df["Volume"])
        volume_ticks_x : int, optional
            Number to multiply volume, by default 7

        Returns
        -------
        Dict[str, list]
            {"range": volume_range, "ticks": tickvals}
        """
        ...
    
    def add_inchart_volume(self, df_stock: pd.DataFrame, close_col: Optional[str] = ..., volume_col: Optional[str] = ..., row: Optional[int] = ..., col: Optional[int] = ..., volume_ticks_x: int = ...) -> None:
        """Add in-chart volume to a subplot.

        Parameters
        ----------
        df_stock : `pd.DataFrame`
            Dataframe of the stock
        close_col : `str`, optional
            Name of the close column, by default "Close"
        volume_col : `str`, optional
            Name of the volume column, by default "Volume"
        row : `int`, optional
            Row number, by default 2
        col : `int`, optional
            Column number, by default 1
        volume_ticks_x : int, optional
            Number to multiply volume, by default 7
        """
        ...
    
    def add_legend_label(self, trace: Optional[str] = ..., label: Optional[str] = ..., mode: Optional[str] = ..., marker: Optional[dict] = ..., line_dash: Optional[str] = ..., legendrank: Optional[int] = ..., **kwargs) -> None:
        """Add a legend label.

        Parameters
        ----------
        trace : `str`, optional
            The name of the trace to use as a template, by default None
        label : `str`, optional
            The label to use, by default None (uses the trace name if trace is specified)
            If trace is not specified, label must be specified
        mode : `str`, optional
            The mode to use, by default "lines" (uses the trace mode if trace is specified)
        marker : `dict`, optional
            The marker to use, by default dict() (uses the trace marker if trace is specified)
        line_dash : `str`, optional
            The line dash to use, by default "solid" (uses the trace line dash if trace is specified)
        legendrank : `int`, optional
            The legend rank, by default None (e.g. 1 is above 2)

        Raises
        ------
        ValueError
            If trace is not found
        ValueError
            If label is not specified and trace is not specified
        """
        ...
    
    def show(self, *args, external: bool = ..., export_image: Optional[Union[Path, str]] = ..., **kwargs) -> Optional[OpenBBFigure]:
        """Show the figure.

        Parameters
        ----------
        external : `bool`, optional
            Whether to return the figure object instead of showing it, by default False
        export_image : `Union[Path, str]`, optional
            The path to export the figure image to, by default ""
        cmd_xshift : `int`, optional
            The x shift of the command source annotation, by default 0
        bar_width : `float`, optional
            The width of the bars, by default 0.0001
        date_xaxis : `bool`, optional
            Whether to check if the xaxis is a date axis, by default True
        """
        ...
    
    def get_subplots_dict(self) -> Dict[str, Dict[str, List[Any]]]:
        """Return the subplots dict.

        Returns
        -------
        `dict`
            The subplots dict
        """
        ...
    
    def get_dateindex(self) -> Optional[List[datetime]]:
        """Return the dateindex of the figure.

        Returns
        -------
        `list`
            The dateindex
        """
        ...
    
    def hide_date_gaps(self, df_data: pd.DataFrame, row: Optional[int] = ..., col: Optional[int] = ...) -> None:
        """Add rangebreaks to hide datetime gaps on the xaxis.

        Parameters
        ----------
        df_data : `pandas.DataFrame`
            The dataframe with the data.
        row : `int`, optional
            The row of the subplot to hide the gaps, by default None
        col : `int`, optional
            The column of the subplot to hide the gaps, by default None
        """
        ...
    
    def add_rangebreaks(self) -> None:
        """Add rangebreaks to hide datetime gaps on the xaxis."""
        ...
    
    def to_subplot(self, subplot: OpenBBFigure, row: int, col: int, secondary_y: bool = ..., **kwargs) -> OpenBBFigure:
        """Return the figure as a subplot of another figure.

        Parameters
        ----------
        subplot : `plotly.graph_objects.Figure`
            The subplot
        row : `int`
            Row number
        col : `int`
            Column number
        secondary_y : `bool`, optional
            Whether to use the secondary y axis, by default False

        Returns
        -------
        `plotly.graph_objects.Figure`
            The subplot with the figure added
        """
        ...
    
    def to_html(self, *args, **kwargs) -> str:
        """Return the figure as HTML."""
        ...
    
    @staticmethod
    def row_colors(data: pd.DataFrame) -> Optional[List[str]]:
        """Return the row colors of the table.

        Parameters
        ----------
        data : `pandas.DataFrame`
            The dataframe

        Returns
        -------
        `list`
            The list of colors
        """
        ...
    
    @classmethod
    def to_table(cls, data: pd.DataFrame, columnwidth: Optional[List[Union[int, float]]] = ..., print_index: bool = ..., **kwargs) -> OpenBBFigure:
        """Convert a dataframe to a table figure.

        Parameters
        ----------
        data : `pandas.DataFrame`
            The dataframe to convert
        columnwidth : `list`, optional
            The width of each column, by default None (auto)
        print_index : `bool`, optional
            Whether to print the index, by default True
        height : `int`, optional
            The height of the table, by default len(data.index) * 28 + 25
        width : `int`, optional
            The width of the table, by default sum(columnwidth) * 8.7

        Returns
        -------
        `plotly.graph_objects.Figure`
            The figure as a table
        """
        ...
    
    def add_logscale_menus(self, yaxis: str = ...) -> None:
        """Set the menus for the figure."""
        ...
    
    def add_corr_plot(self, series: pd.DataFrame, max_lag: int = ..., m: Optional[int] = ..., alpha: Optional[float] = ..., marker: Optional[dict] = ..., row: Optional[int] = ..., col: Optional[int] = ..., pacf: bool = ..., **kwargs) -> None:
        """Add a correlation plot to a figure object.

        Parameters
        ----------
        fig : OpenBBFigure
            Figure object to add plot to
        series : pd.DataFrame
            Dataframe to look at
        max_lag : int, optional
            Number of lags to look at, by default 15
        m: Optional[int]
            Optionally, a time lag to highlight on the plot. Default is none.
        alpha: Optional[float]
            Optionally, a significance level to highlight on the plot. Default is 0.05.
        row : int, optional
            Row to add plot to, by default None
        col : int, optional
            Column to add plot to, by default None
        pacf : bool, optional
            Flag to indicate whether to use partial autocorrelation or not, by default False
        """
        ...
    


