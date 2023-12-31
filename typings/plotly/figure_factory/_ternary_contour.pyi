"""
This type stub file was generated by pyright.
"""

np = ...
scipy_interp = ...
def create_ternary_contour(coordinates, values, pole_labels=..., width=..., height=..., ncontours=..., showscale=..., coloring=..., colorscale=..., linecolor=..., title=..., interp_mode=..., showmarkers=...): # -> Figure:
    """
    Ternary contour plot.

    Parameters
    ----------

    coordinates : list or ndarray
        Barycentric coordinates of shape (2, N) or (3, N) where N is the
        number of data points. The sum of the 3 coordinates is expected
        to be 1 for all data points.
    values : array-like
        Data points of field to be represented as contours.
    pole_labels : str, default ['a', 'b', 'c']
        Names of the three poles of the triangle.
    width : int
        Figure width.
    height : int
        Figure height.
    ncontours : int or None
        Number of contours to display (determined automatically if None).
    showscale : bool, default False
        If True, a colorbar showing the color scale is displayed.
    coloring : None or 'lines'
        How to display contour. Filled contours if None, lines if ``lines``.
    colorscale : None or str (Plotly colormap)
        colorscale of the contours.
    linecolor : None or rgb color
        Color used for lines. ``colorscale`` has to be set to None, otherwise
        line colors are determined from ``colorscale``.
    title : str or None
        Title of ternary plot
    interp_mode : 'ilr' (default) or 'cartesian'
        Defines how data are interpolated to compute contours. If 'irl',
        ILR (Isometric Log-Ratio) of compositional data is performed. If
        'cartesian', contours are determined in Cartesian space.
    showmarkers : bool, default False
        If True, markers corresponding to input compositional points are
        superimposed on contours, using the same colorscale.

    Examples
    ========

    Example 1: ternary contour plot with filled contours

    >>> import plotly.figure_factory as ff
    >>> import numpy as np
    >>> # Define coordinates
    >>> a, b = np.mgrid[0:1:20j, 0:1:20j]
    >>> mask = a + b <= 1
    >>> a = a[mask].ravel()
    >>> b = b[mask].ravel()
    >>> c = 1 - a - b
    >>> # Values to be displayed as contours
    >>> z = a * b * c
    >>> fig = ff.create_ternary_contour(np.stack((a, b, c)), z)
    >>> fig.show()

    It is also possible to give only two barycentric coordinates for each
    point, since the sum of the three coordinates is one:

    >>> fig = ff.create_ternary_contour(np.stack((a, b)), z)


    Example 2: ternary contour plot with line contours

    >>> fig = ff.create_ternary_contour(np.stack((a, b, c)), z, coloring='lines')

    Example 3: customize number of contours

    >>> fig = ff.create_ternary_contour(np.stack((a, b, c)), z, ncontours=8)

    Example 4: superimpose contour plot and original data as markers

    >>> fig = ff.create_ternary_contour(np.stack((a, b, c)), z, coloring='lines',
    ...                                 showmarkers=True)

    Example 5: customize title and pole labels

    >>> fig = ff.create_ternary_contour(np.stack((a, b, c)), z,
    ...                                 title='Ternary plot',
    ...                                 pole_labels=['clay', 'quartz', 'fledspar'])
    """
    ...

