"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Line(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def color(self): # -> tuple[Unknown, ...] | Line | None:
        """
        Sets the color of the line enclosing each sector. Defaults to
        the `paper_bgcolor` value.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        ...
    
    @color.setter
    def color(self, val): # -> None:
        ...
    
    @property
    def colorsrc(self): # -> tuple[Unknown, ...] | Line | None:
        """
        Sets the source reference on Chart Studio Cloud for `color`.

        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @colorsrc.setter
    def colorsrc(self, val): # -> None:
        ...
    
    @property
    def width(self): # -> tuple[Unknown, ...] | Line | None:
        """
        Sets the width (in px) of the line enclosing each sector.

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [0, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        ...
    
    @width.setter
    def width(self, val): # -> None:
        ...
    
    @property
    def widthsrc(self): # -> tuple[Unknown, ...] | Line | None:
        """
        Sets the source reference on Chart Studio Cloud for `width`.

        The 'widthsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @widthsrc.setter
    def widthsrc(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., color=..., colorsrc=..., width=..., widthsrc=..., **kwargs) -> None:
        """
        Construct a new Line object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.treemap.marker.Line`
        color
            Sets the color of the line enclosing each sector.
            Defaults to the `paper_bgcolor` value.
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        width
            Sets the width (in px) of the line enclosing each
            sector.
        widthsrc
            Sets the source reference on Chart Studio Cloud for
            `width`.

        Returns
        -------
        Line
        """
        ...
    


