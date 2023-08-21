"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Tiling(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def flip(self): # -> tuple[Unknown, ...] | Tiling | None:
        """
        Determines if the positions obtained from solver are flipped on
        each axis.

        The 'flip' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y'] joined with '+' characters
            (e.g. 'x+y')

        Returns
        -------
        Any
        """
        ...
    
    @flip.setter
    def flip(self, val): # -> None:
        ...
    
    @property
    def orientation(self): # -> tuple[Unknown, ...] | Tiling | None:
        """
        When set in conjunction with `tiling.flip`, determines on which
        side the root nodes are drawn in the chart. If
        `tiling.orientation` is "v" and `tiling.flip` is "", the root
        nodes appear at the top. If `tiling.orientation` is "v" and
        `tiling.flip` is "y", the root nodes appear at the bottom. If
        `tiling.orientation` is "h" and `tiling.flip` is "", the root
        nodes appear at the left. If `tiling.orientation` is "h" and
        `tiling.flip` is "x", the root nodes appear at the right.

        The 'orientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['v', 'h']

        Returns
        -------
        Any
        """
        ...
    
    @orientation.setter
    def orientation(self, val): # -> None:
        ...
    
    @property
    def pad(self): # -> tuple[Unknown, ...] | Tiling | None:
        """
        Sets the inner padding (in px).

        The 'pad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @pad.setter
    def pad(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., flip=..., orientation=..., pad=..., **kwargs) -> None:
        """
        Construct a new Tiling object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.icicle.Tiling`
        flip
            Determines if the positions obtained from solver are
            flipped on each axis.
        orientation
            When set in conjunction with `tiling.flip`, determines
            on which side the root nodes are drawn in the chart. If
            `tiling.orientation` is "v" and `tiling.flip` is "",
            the root nodes appear at the top. If
            `tiling.orientation` is "v" and `tiling.flip` is "y",
            the root nodes appear at the bottom. If
            `tiling.orientation` is "h" and `tiling.flip` is "",
            the root nodes appear at the left. If
            `tiling.orientation` is "h" and `tiling.flip` is "x",
            the root nodes appear at the right.
        pad
            Sets the inner padding (in px).

        Returns
        -------
        Tiling
        """
        ...
    


