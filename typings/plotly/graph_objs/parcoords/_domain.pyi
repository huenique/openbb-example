"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Domain(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def column(self): # -> tuple[Unknown, ...] | Domain | None:
        """
        If there is a layout grid, use the domain for this column in
        the grid for this parcoords trace .

        The 'column' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        ...
    
    @column.setter
    def column(self, val): # -> None:
        ...
    
    @property
    def row(self): # -> tuple[Unknown, ...] | Domain | None:
        """
        If there is a layout grid, use the domain for this row in the
        grid for this parcoords trace .

        The 'row' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        ...
    
    @row.setter
    def row(self, val): # -> None:
        ...
    
    @property
    def x(self): # -> tuple[Unknown, ...] | Domain | None:
        """
            Sets the horizontal domain of this parcoords trace (in plot
            fraction).

            The 'x' property is an info array that may be specified as:

            * a list or tuple of 2 elements where:
        (0) The 'x[0]' property is a number and may be specified as:
              - An int or float in the interval [0, 1]
        (1) The 'x[1]' property is a number and may be specified as:
              - An int or float in the interval [0, 1]

            Returns
            -------
            list
        """
        ...
    
    @x.setter
    def x(self, val): # -> None:
        ...
    
    @property
    def y(self): # -> tuple[Unknown, ...] | Domain | None:
        """
            Sets the vertical domain of this parcoords trace (in plot
            fraction).

            The 'y' property is an info array that may be specified as:

            * a list or tuple of 2 elements where:
        (0) The 'y[0]' property is a number and may be specified as:
              - An int or float in the interval [0, 1]
        (1) The 'y[1]' property is a number and may be specified as:
              - An int or float in the interval [0, 1]

            Returns
            -------
            list
        """
        ...
    
    @y.setter
    def y(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., column=..., row=..., x=..., y=..., **kwargs) -> None:
        """
        Construct a new Domain object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.parcoords.Domain`
        column
            If there is a layout grid, use the domain for this
            column in the grid for this parcoords trace .
        row
            If there is a layout grid, use the domain for this row
            in the grid for this parcoords trace .
        x
            Sets the horizontal domain of this parcoords trace (in
            plot fraction).
        y
            Sets the vertical domain of this parcoords trace (in
            plot fraction).

        Returns
        -------
        Domain
        """
        ...
    


