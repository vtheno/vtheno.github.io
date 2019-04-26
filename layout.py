class auto(object):
    auto = "auto"


class axis(object):
    """
    flex-direction: row | row-reverse | column | column-reverse
    """

    row = "row"
    column = "column"
    row_reverse = "row-reverse"
    column_reverse = "column-reverse"


class wrap(object):
    """
    flex-wrap: nowrap | wrap | wrap-reverse
    """

    wrap = "wrap"
    nowrap = "nowrap"
    wrap_reverse = "wrap-reverse"


class axisMain(object):
    """
    justify-content: flex-start | flex-end | center | space-between | space-around
    """

    start = "flex-start"
    center = "center"
    end = "flex-end"
    between = "space-between"
    around = "space-around"


class axisCross(object):
    """
    align-items: flex-start | flex-end | center | baseline | stretch;
    """

    start = "flex-start"
    center = "center"
    end = "flex-end"
    baseline = "baseline"
    stretch = "stretch"


class itemSelf(object):
    """
    align-self: flex-start | flex-end | center | baseline | stretch;
    """

    start = "flex-start"
    center = "center"
    end = "flex-end"
    baseline = "baseline"
    stretch = "stretch"


"""
align-items 适用于所有flex容器内item的对齐方式
align-content 适用于多行flex容器内item的对齐方式 单行容器无效
align-self 控制item本身在flex容器 中的对齐方式
"""

setitem = dict.__setitem__
maps = {
    "axis": "flex-direction",
    "wrap": "flex-wrap",
    "axisMain": "justify-content",
    "axisCross": "align-items",
    "itemSelf": "align-self",
    "order": "order",
    "grow": "flex-grow",
    "shrink": "flex-shrink",
    "basis": "flex-basis",
    "height": "height",
    "width": "width",
    "color": "color",
    "background": "background",
    "overflow": "overflow",
    "box-sizing": "box-sizing",
    "box-shadow": "box-shadow",
    "margin": "margin",
    "margin-top": "margin-top",
    "margin-bottom": "margin-bottom",
    "margin-left": "margin-left",
    "margin-right": "margin-right",
    "padding": "padding",
    "padding-top": "padding-top",
    "padding-bottom": "padding-bottom",
    "padding-left": "padding-left",
    "padding-right": "padding-right",
}
allows = [
    "axis",
    "wrap",
    "axisMain",
    "axisCross",
    "itemSelf",
    "order",
    "grow",
    "shrink",
    "basis",
    "height",
    "width",
    "color",
    "background",
    "overflow",
    "box-sizing",
    "box-shadow",
    "margin",
    "margin-top",
    "margin-bottom",
    "margin-left",
    "margin-right",
    "padding",
    "padding-top",
    "padding-bottom",
    "padding-left",
    "padding-right",
]


class layout(dict):
    def __init__(self, name: str):
        self.name = name
        dict.__init__(self)
        # default
        setitem(self, "display", "flex")
        # setitem(self, "width", "inherit") # 100%;
        # setitem(self, "height", "inherit") # 100%;
        setitem(self, "overflow", "visible")
        setitem(self, "box-sizing", "border-box") # default to border-box not content-box
        setitem(self, "margin", "0")
        setitem(self, "padding", "0")
        # init
        setitem(self, "flex-direction", axis.row)  # axis
        # wrap
        setitem(self, "flex-wrap", wrap.nowrap)  # rap
        # axisMain
        setitem(self, "justify-content", axisMain.start)  # axisMain
        # axisCross
        setitem(self, "align-items", axisCross.start)  # axisCross
        setitem(self, "flex-grow", "1")  # int | auto
        setitem(self, "flex-shrink", "1")  # int | auto
        setitem(self, "flex-basis", auto.auto)  # str | auto

    def __str__(self):
        body = " ".join("{}: {};".format(k, str(v)) for k, v in self.items())
        return ".{} {{\n{}\n}}".format(self.name, body)

    def __setitem__(self, name: str, value: object) -> ():
        if name in allows:
            setitem(self, maps[name], value)


__all__ = ["auto", "axis", "axisMain", "axisCross", "wrap", "layout"]
