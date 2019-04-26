from layout import auto, axis, axisMain, axisCross, wrap, layout
from build_tool import build_style, build_body, build_template

outer = layout("outer")
header = layout("header")
content = layout("content")

outer["width"] = "100%"
outer["height"] = "100%"
outer["axis"] = axis.column
# basis is height, because of outer axis is column
header["basis"] = "8%"
header["width"] = "100%"
header["axis"] = axis.column
header["overflow"] = "visible"

content["basis"] = "92%"
content["width"] = "100%"
content["overflow"] = auto.auto
content["axis"] = axis.column
content["axisMain"] = axisMain.center
content["axisCross"] = axisCross.center

# outer: width 500px
# div1: basis 100px shrink 1
# div2: basis 200px shrink 2
# div3: basis 300px shrink 3
# this is shrink calc method
# weight = 100px * 1 + 200px * 2 + 300px * 3 = 1400px
# offset = sum div - parent = 100px + 200px + 300px - 500px = 100px
# div1 real size:
# calc size = 100px - (100px * 1 / 1400px * offset) = 92.86px
# div2 real size:
# calc size = 200px - (200px * 2 / 1400px * offset) = 171.42px
# div3 real size:
# calc size = 300px - (300px * 3 / 1400px * offset) = 235.71px

# if requrie grow calc method
# offset = parent - sum div
# calc size = basis + (basis * grow / weight * offset)

style = build_style(outer, header, content)
body = build_body("app.html")
output = build_template("demo", style, body)
with open("index.html", "w", encoding="utf8") as file:
    file.write(output)
