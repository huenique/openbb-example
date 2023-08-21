"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Updatemenu(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def active(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Determines which button (by index starting from 0) is
        considered active.

        The 'active' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [-1, 9223372036854775807]

        Returns
        -------
        int
        """
        ...
    
    @active.setter
    def active(self, val): # -> None:
        ...
    
    @property
    def bgcolor(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Sets the background color of the update menu buttons.

        The 'bgcolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        ...
    
    @bgcolor.setter
    def bgcolor(self, val): # -> None:
        ...
    
    @property
    def bordercolor(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Sets the color of the border enclosing the update menu.

        The 'bordercolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        ...
    
    @bordercolor.setter
    def bordercolor(self, val): # -> None:
        ...
    
    @property
    def borderwidth(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Sets the width (in px) of the border enclosing the update menu.

        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @borderwidth.setter
    def borderwidth(self, val): # -> None:
        ...
    
    @property
    def buttons(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        The 'buttons' property is a tuple of instances of
        Button that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.updatemenu.Button
          - A list or tuple of dicts of string/value properties that
            will be passed to the Button constructor

            Supported dict properties:

                args
                    Sets the arguments values to be passed to the
                    Plotly method set in `method` on click.
                args2
                    Sets a 2nd set of `args`, these arguments
                    values are passed to the Plotly method set in
                    `method` when clicking this button while in the
                    active state. Use this to create toggle
                    buttons.
                execute
                    When true, the API method is executed. When
                    false, all other behaviors are the same and
                    command execution is skipped. This may be
                    useful when hooking into, for example, the
                    `plotly_buttonclicked` method and executing the
                    API command manually without losing the benefit
                    of the updatemenu automatically binding to the
                    state of the plot through the specification of
                    `method` and `args`.
                label
                    Sets the text label to appear on the button.
                method
                    Sets the Plotly method to be called on click.
                    If the `skip` method is used, the API
                    updatemenu will function as normal but will
                    perform no API calls and will not bind
                    automatically to state updates. This may be
                    used to create a component interface and attach
                    to updatemenu events manually via JavaScript.
                name
                    When used in a template, named items are
                    created in the output figure in addition to any
                    items the figure already has in this array. You
                    can modify these items in the output figure by
                    making your own item with `templateitemname`
                    matching this `name` alongside your
                    modifications (including `visible: false` or
                    `enabled: false` to hide it). Has no effect
                    outside of a template.
                templateitemname
                    Used to refer to a named item in this array in
                    the template. Named items from the template
                    will be created even without a matching item in
                    the input figure, but you can modify one by
                    making an item with `templateitemname` matching
                    its `name`, alongside your modifications
                    (including `visible: false` or `enabled: false`
                    to hide it). If there is no template or no
                    matching item, this item will be hidden unless
                    you explicitly show it with `visible: true`.
                visible
                    Determines whether or not this button is
                    visible.

        Returns
        -------
        tuple[plotly.graph_objs.layout.updatemenu.Button]
        """
        ...
    
    @buttons.setter
    def buttons(self, val): # -> None:
        ...
    
    @property
    def buttondefaults(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        When used in a template (as
        layout.template.layout.updatemenu.buttondefaults), sets the
        default property values to use for elements of
        layout.updatemenu.buttons

        The 'buttondefaults' property is an instance of Button
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.updatemenu.Button`
          - A dict of string/value properties that will be passed
            to the Button constructor

            Supported dict properties:

        Returns
        -------
        plotly.graph_objs.layout.updatemenu.Button
        """
        ...
    
    @buttondefaults.setter
    def buttondefaults(self, val): # -> None:
        ...
    
    @property
    def direction(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Determines the direction in which the buttons are laid out,
        whether in a dropdown menu or a row/column of buttons. For
        `left` and `up`, the buttons will still appear in left-to-right
        or top-to-bottom order respectively.

        The 'direction' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'right', 'up', 'down']

        Returns
        -------
        Any
        """
        ...
    
    @direction.setter
    def direction(self, val): # -> None:
        ...
    
    @property
    def font(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Sets the font of the update menu button text.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.updatemenu.Font`
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
        plotly.graph_objs.layout.updatemenu.Font
        """
        ...
    
    @font.setter
    def font(self, val): # -> None:
        ...
    
    @property
    def name(self): # -> tuple[Unknown, ...] | Updatemenu | None:
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
    def pad(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Sets the padding around the buttons or dropdown menu.

        The 'pad' property is an instance of Pad
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.updatemenu.Pad`
          - A dict of string/value properties that will be passed
            to the Pad constructor

            Supported dict properties:

                b
                    The amount of padding (in px) along the bottom
                    of the component.
                l
                    The amount of padding (in px) on the left side
                    of the component.
                r
                    The amount of padding (in px) on the right side
                    of the component.
                t
                    The amount of padding (in px) along the top of
                    the component.

        Returns
        -------
        plotly.graph_objs.layout.updatemenu.Pad
        """
        ...
    
    @pad.setter
    def pad(self, val): # -> None:
        ...
    
    @property
    def showactive(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Highlights active dropdown item or active button if true.

        The 'showactive' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @showactive.setter
    def showactive(self, val): # -> None:
        ...
    
    @property
    def templateitemname(self): # -> tuple[Unknown, ...] | Updatemenu | None:
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
    def type(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Determines whether the buttons are accessible via a dropdown
        menu or whether the buttons are stacked horizontally or
        vertically

        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['dropdown', 'buttons']

        Returns
        -------
        Any
        """
        ...
    
    @type.setter
    def type(self, val): # -> None:
        ...
    
    @property
    def visible(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Determines whether or not the update menu is visible.

        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @visible.setter
    def visible(self, val): # -> None:
        ...
    
    @property
    def x(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Sets the x position (in normalized coordinates) of the update
        menu.

        The 'x' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        ...
    
    @x.setter
    def x(self, val): # -> None:
        ...
    
    @property
    def xanchor(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Sets the update menu's horizontal position anchor. This anchor
        binds the `x` position to the "left", "center" or "right" of
        the range selector.

        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        ...
    
    @xanchor.setter
    def xanchor(self, val): # -> None:
        ...
    
    @property
    def y(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Sets the y position (in normalized coordinates) of the update
        menu.

        The 'y' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        ...
    
    @y.setter
    def y(self, val): # -> None:
        ...
    
    @property
    def yanchor(self): # -> tuple[Unknown, ...] | Updatemenu | None:
        """
        Sets the update menu's vertical position anchor This anchor
        binds the `y` position to the "top", "middle" or "bottom" of
        the range selector.

        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        ...
    
    @yanchor.setter
    def yanchor(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., active=..., bgcolor=..., bordercolor=..., borderwidth=..., buttons=..., buttondefaults=..., direction=..., font=..., name=..., pad=..., showactive=..., templateitemname=..., type=..., visible=..., x=..., xanchor=..., y=..., yanchor=..., **kwargs) -> None:
        """
        Construct a new Updatemenu object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.Updatemenu`
        active
            Determines which button (by index starting from 0) is
            considered active.
        bgcolor
            Sets the background color of the update menu buttons.
        bordercolor
            Sets the color of the border enclosing the update menu.
        borderwidth
            Sets the width (in px) of the border enclosing the
            update menu.
        buttons
            A tuple of
            :class:`plotly.graph_objects.layout.updatemenu.Button`
            instances or dicts with compatible properties
        buttondefaults
            When used in a template (as
            layout.template.layout.updatemenu.buttondefaults), sets
            the default property values to use for elements of
            layout.updatemenu.buttons
        direction
            Determines the direction in which the buttons are laid
            out, whether in a dropdown menu or a row/column of
            buttons. For `left` and `up`, the buttons will still
            appear in left-to-right or top-to-bottom order
            respectively.
        font
            Sets the font of the update menu button text.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        pad
            Sets the padding around the buttons or dropdown menu.
        showactive
            Highlights active dropdown item or active button if
            true.
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
        type
            Determines whether the buttons are accessible via a
            dropdown menu or whether the buttons are stacked
            horizontally or vertically
        visible
            Determines whether or not the update menu is visible.
        x
            Sets the x position (in normalized coordinates) of the
            update menu.
        xanchor
            Sets the update menu's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            update menu.
        yanchor
            Sets the update menu's vertical position anchor This
            anchor binds the `y` position to the "top", "middle" or
            "bottom" of the range selector.

        Returns
        -------
        Updatemenu
        """
        ...
    


