"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Title(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def font(self): # -> tuple[Unknown, ...] | Title | None:
        """
        Sets this axis' title font. Note that the title's font used to
        be customized by the now deprecated `titlefont` attribute.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.scene.yaxis.title.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

            Supported dict properties:

                color

                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The Chart Studio Cloud (at
                    https://chart-studio.plotly.com or on-premise)
                    generates images on a server, where only a
                    select number of fonts are installed and
                    supported. These include "Arial", "Balto",
                    "Courier New", "Droid Sans",, "Droid Serif",
                    "Droid Sans Mono", "Gravitas One", "Old
                    Standard TT", "Open Sans", "Overpass", "PT Sans
                    Narrow", "Raleway", "Times New Roman".
                size

        Returns
        -------
        plotly.graph_objs.layout.scene.yaxis.title.Font
        """
        ...
    
    @font.setter
    def font(self, val): # -> None:
        ...
    
    @property
    def text(self): # -> tuple[Unknown, ...] | Title | None:
        """
        Sets the title of this axis. Note that before the existence of
        `title.text`, the title's contents used to be defined as the
        `title` attribute itself. This behavior has been deprecated.

        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @text.setter
    def text(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., font=..., text=..., **kwargs) -> None:
        """
        Construct a new Title object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.scene.yaxis.Title`
        font
            Sets this axis' title font. Note that the title's font
            used to be customized by the now deprecated `titlefont`
            attribute.
        text
            Sets the title of this axis. Note that before the
            existence of `title.text`, the title's contents used to
            be defined as the `title` attribute itself. This
            behavior has been deprecated.

        Returns
        -------
        Title
        """
        ...
    


