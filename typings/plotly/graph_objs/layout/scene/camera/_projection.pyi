"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Projection(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def type(self): # -> tuple[Unknown, ...] | Projection | None:
        """
        Sets the projection type. The projection type could be either
        "perspective" or "orthographic". The default is "perspective".

        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['perspective', 'orthographic']

        Returns
        -------
        Any
        """
        ...
    
    @type.setter
    def type(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., type=..., **kwargs) -> None:
        """
        Construct a new Projection object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.scene.c
            amera.Projection`
        type
            Sets the projection type. The projection type could be
            either "perspective" or "orthographic". The default is
            "perspective".

        Returns
        -------
        Projection
        """
        ...
    

