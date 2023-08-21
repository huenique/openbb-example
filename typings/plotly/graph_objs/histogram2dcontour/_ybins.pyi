"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class YBins(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def end(self): # -> tuple[Unknown, ...] | YBins | None:
        """
        Sets the end value for the y axis bins. The last bin may not
        end exactly at this value, we increment the bin edge by `size`
        from `start` until we reach or exceed `end`. Defaults to the
        maximum data value. Like `start`, for dates use a date string,
        and for category data `end` is based on the category serial
        numbers.

        The 'end' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @end.setter
    def end(self, val): # -> None:
        ...
    
    @property
    def size(self): # -> tuple[Unknown, ...] | YBins | None:
        """
        Sets the size of each y axis bin. Default behavior: If `nbinsy`
        is 0 or omitted, we choose a nice round bin size such that the
        number of bins is about the same as the typical number of
        samples in each bin. If `nbinsy` is provided, we choose a nice
        round bin size giving no more than that many bins. For date
        data, use milliseconds or "M<n>" for months, as in
        `axis.dtick`. For category data, the number of categories to
        bin together (always defaults to 1).

        The 'size' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @size.setter
    def size(self, val): # -> None:
        ...
    
    @property
    def start(self): # -> tuple[Unknown, ...] | YBins | None:
        """
        Sets the starting value for the y axis bins. Defaults to the
        minimum data value, shifted down if necessary to make nice
        round values and to remove ambiguous bin edges. For example, if
        most of the data is integers we shift the bin edges 0.5 down,
        so a `size` of 5 would have a default `start` of -0.5, so it is
        clear that 0-4 are in the first bin, 5-9 in the second, but
        continuous data gets a start of 0 and bins [0,5), [5,10) etc.
        Dates behave similarly, and `start` should be a date string.
        For category data, `start` is based on the category serial
        numbers, and defaults to -0.5.

        The 'start' property accepts values of any type

        Returns
        -------
        Any
        """
        ...
    
    @start.setter
    def start(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., end=..., size=..., start=..., **kwargs) -> None:
        """
        Construct a new YBins object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.histogram2dcontour.YBins`
        end
            Sets the end value for the y axis bins. The last bin
            may not end exactly at this value, we increment the bin
            edge by `size` from `start` until we reach or exceed
            `end`. Defaults to the maximum data value. Like
            `start`, for dates use a date string, and for category
            data `end` is based on the category serial numbers.
        size
            Sets the size of each y axis bin. Default behavior: If
            `nbinsy` is 0 or omitted, we choose a nice round bin
            size such that the number of bins is about the same as
            the typical number of samples in each bin. If `nbinsy`
            is provided, we choose a nice round bin size giving no
            more than that many bins. For date data, use
            milliseconds or "M<n>" for months, as in `axis.dtick`.
            For category data, the number of categories to bin
            together (always defaults to 1).
        start
            Sets the starting value for the y axis bins. Defaults
            to the minimum data value, shifted down if necessary to
            make nice round values and to remove ambiguous bin
            edges. For example, if most of the data is integers we
            shift the bin edges 0.5 down, so a `size` of 5 would
            have a default `start` of -0.5, so it is clear that 0-4
            are in the first bin, 5-9 in the second, but continuous
            data gets a start of 0 and bins [0,5), [5,10) etc.
            Dates behave similarly, and `start` should be a date
            string. For category data, `start` is based on the
            category serial numbers, and defaults to -0.5.

        Returns
        -------
        YBins
        """
        ...
    


