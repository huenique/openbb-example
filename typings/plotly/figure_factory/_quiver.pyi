"""
This type stub file was generated by pyright.
"""

def create_quiver(x, y, u, v, scale=..., arrow_scale=..., angle=..., scaleratio=..., **kwargs): # -> Figure:
    """
    Returns data for a quiver plot.

    :param (list|ndarray) x: x coordinates of the arrow locations
    :param (list|ndarray) y: y coordinates of the arrow locations
    :param (list|ndarray) u: x components of the arrow vectors
    :param (list|ndarray) v: y components of the arrow vectors
    :param (float in [0,1]) scale: scales size of the arrows(ideally to
        avoid overlap). Default = .1
    :param (float in [0,1]) arrow_scale: value multiplied to length of barb
        to get length of arrowhead. Default = .3
    :param (angle in radians) angle: angle of arrowhead. Default = pi/9
    :param (positive float) scaleratio: the ratio between the scale of the y-axis
        and the scale of the x-axis (scale_y / scale_x). Default = None, the
        scale ratio is not fixed.
    :param kwargs: kwargs passed through plotly.graph_objs.Scatter
        for more information on valid kwargs call
        help(plotly.graph_objs.Scatter)

    :rtype (dict): returns a representation of quiver figure.

    Example 1: Trivial Quiver

    >>> from plotly.figure_factory import create_quiver
    >>> import math

    >>> # 1 Arrow from (0,0) to (1,1)
    >>> fig = create_quiver(x=[0], y=[0], u=[1], v=[1], scale=1)
    >>> fig.show()


    Example 2: Quiver plot using meshgrid

    >>> from plotly.figure_factory import create_quiver

    >>> import numpy as np
    >>> import math

    >>> # Add data
    >>> x,y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
    >>> u = np.cos(x)*y
    >>> v = np.sin(x)*y

    >>> #Create quiver
    >>> fig = create_quiver(x, y, u, v)
    >>> fig.show()


    Example 3: Styling the quiver plot

    >>> from plotly.figure_factory import create_quiver
    >>> import numpy as np
    >>> import math

    >>> # Add data
    >>> x, y = np.meshgrid(np.arange(-np.pi, math.pi, .5),
    ...                    np.arange(-math.pi, math.pi, .5))
    >>> u = np.cos(x)*y
    >>> v = np.sin(x)*y

    >>> # Create quiver
    >>> fig = create_quiver(x, y, u, v, scale=.2, arrow_scale=.3, angle=math.pi/6,
    ...                     name='Wind Velocity', line=dict(width=1))

    >>> # Add title to layout
    >>> fig.update_layout(title='Quiver Plot') # doctest: +SKIP
    >>> fig.show()


    Example 4: Forcing a fix scale ratio to maintain the arrow length

    >>> from plotly.figure_factory import create_quiver
    >>> import numpy as np

    >>> # Add data
    >>> x,y = np.meshgrid(np.arange(0.5, 3.5, .5), np.arange(0.5, 4.5, .5))
    >>> u = x
    >>> v = y
    >>> angle = np.arctan(v / u)
    >>> norm = 0.25
    >>> u = norm * np.cos(angle)
    >>> v = norm * np.sin(angle)

    >>> # Create quiver with a fix scale ratio
    >>> fig = create_quiver(x, y, u, v, scale = 1, scaleratio = 0.5)
    >>> fig.show()
    """
    ...

class _Quiver:
    """
    Refer to FigureFactory.create_quiver() for docstring
    """
    def __init__(self, x, y, u, v, scale, arrow_scale, angle, scaleratio=..., **kwargs) -> None:
        ...
    
    def scale_uv(self): # -> None:
        """
        Scales u and v to avoid overlap of the arrows.

        u and v are added to x and y to get the
        endpoints of the arrows so a smaller scale value will
        result in less overlap of arrows.
        """
        ...
    
    def get_barbs(self): # -> tuple[list[Unknown | None], list[Unknown | None]]:
        """
        Creates x and y startpoint and endpoint pairs

        After finding the endpoint of each barb this zips startpoint and
        endpoint pairs to create 2 lists: x_values for barbs and y values
        for barbs

        :rtype: (list, list) barb_x, barb_y: list of startpoint and endpoint
            x_value pairs separated by a None to create the barb of the arrow,
            and list of startpoint and endpoint y_value pairs separated by a
            None to create the barb of the arrow.
        """
        ...
    
    def get_quiver_arrows(self): # -> tuple[list[Unknown | None], list[Unknown | None]]:
        """
        Creates lists of x and y values to plot the arrows

        Gets length of each barb then calculates the length of each side of
        the arrow. Gets angle of barb and applies angle to each side of the
        arrowhead. Next uses arrow_scale to scale the length of arrowhead and
        creates x and y values for arrowhead point1 and point2. Finally x and y
        values for point1, endpoint and point2s for each arrowhead are
        separated by a None and zipped to create lists of x and y values for
        the arrows.

        :rtype: (list, list) arrow_x, arrow_y: list of point1, endpoint, point2
            x_values separated by a None to create the arrowhead and list of
            point1, endpoint, point2 y_values separated by a None to create
            the barb of the arrow.
        """
        ...
    


