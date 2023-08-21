"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Rangebreak(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def bounds(self): # -> tuple[Unknown, ...] | Rangebreak | None:
        """
            Sets the lower and upper bounds of this axis rangebreak. Can be
            used with `pattern`.

            The 'bounds' property is an info array that may be specified as:

            * a list or tuple of 2 elements where:
        (0) The 'bounds[0]' property accepts values of any type
        (1) The 'bounds[1]' property accepts values of any type

            Returns
            -------
            list
        """
        ...
    
    @bounds.setter
    def bounds(self, val): # -> None:
        ...
    
    @property
    def dvalue(self): # -> tuple[Unknown, ...] | Rangebreak | None:
        """
        Sets the size of each `values` item. The default is one day in
        milliseconds.

        The 'dvalue' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @dvalue.setter
    def dvalue(self, val): # -> None:
        ...
    
    @property
    def enabled(self): # -> tuple[Unknown, ...] | Rangebreak | None:
        """
        Determines whether this axis rangebreak is enabled or disabled.
        Please note that `rangebreaks` only work for "date" axis type.

        The 'enabled' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @enabled.setter
    def enabled(self, val): # -> None:
        ...
    
    @property
    def name(self): # -> tuple[Unknown, ...] | Rangebreak | None:
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.

        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @name.setter
    def name(self, val): # -> None:
        ...
    
    @property
    def pattern(self): # -> tuple[Unknown, ...] | Rangebreak | None:
        """
        Determines a pattern on the time line that generates breaks. If
        *day of week* - days of the week in English e.g. 'Sunday' or
        `sun` (matching is case-insensitive and considers only the
        first three characters), as well as Sunday-based integers
        between 0 and 6. If "hour" - hour (24-hour clock) as decimal
        numbers between 0 and 24. for more info. Examples: - { pattern:
        'day of week', bounds: [6, 1] }  or simply { bounds: ['sat',
        'mon'] }   breaks from Saturday to Monday (i.e. skips the
        weekends). - { pattern: 'hour', bounds: [17, 8] }   breaks from
        5pm to 8am (i.e. skips non-work hours).

        The 'pattern' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['day of week', 'hour', '']

        Returns
        -------
        Any
        """
        ...
    
    @pattern.setter
    def pattern(self, val): # -> None:
        ...
    
    @property
    def templateitemname(self): # -> tuple[Unknown, ...] | Rangebreak | None:
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.

        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @templateitemname.setter
    def templateitemname(self, val): # -> None:
        ...
    
    @property
    def values(self): # -> tuple[Unknown, ...] | Rangebreak | None:
        """
        Sets the coordinate values corresponding to the rangebreaks. An
        alternative to `bounds`. Use `dvalue` to set the size of the
        values along the axis.

        The 'values' property is an info array that may be specified as:
        * a list of elements where:
          The 'values[i]' property accepts values of any type

        Returns
        -------
        list
        """
        ...
    
    @values.setter
    def values(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., bounds=..., dvalue=..., enabled=..., name=..., pattern=..., templateitemname=..., values=..., **kwargs) -> None:
        """
        Construct a new Rangebreak object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.yaxis.Rangebreak`
        bounds
            Sets the lower and upper bounds of this axis
            rangebreak. Can be used with `pattern`.
        dvalue
            Sets the size of each `values` item. The default is one
            day in milliseconds.
        enabled
            Determines whether this axis rangebreak is enabled or
            disabled. Please note that `rangebreaks` only work for
            "date" axis type.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        pattern
            Determines a pattern on the time line that generates
            breaks. If *day of week* - days of the week in English
            e.g. 'Sunday' or `sun` (matching is case-insensitive
            and considers only the first three characters), as well
            as Sunday-based integers between 0 and 6. If "hour" -
            hour (24-hour clock) as decimal numbers between 0 and
            24. for more info. Examples: - { pattern: 'day of
            week', bounds: [6, 1] }  or simply { bounds: ['sat',
            'mon'] }   breaks from Saturday to Monday (i.e. skips
            the weekends). - { pattern: 'hour', bounds: [17, 8] }
            breaks from 5pm to 8am (i.e. skips non-work hours).
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        values
            Sets the coordinate values corresponding to the
            rangebreaks. An alternative to `bounds`. Use `dvalue`
            to set the size of the values along the axis.

        Returns
        -------
        Rangebreak
        """
        ...
    

