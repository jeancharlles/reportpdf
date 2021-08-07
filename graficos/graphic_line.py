from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF

# Definition
d = Drawing(width=400, height=200)
data = [
    (13, 5, 20, 22, 37, 45, 19, 4),
    (5, 20, 46, 38, 23, 21, 6, 14),
]

# Type Chart
lc = HorizontalLineChart()

# Property
lc.x = 50
lc.y = 50
lc.width = 300
lc.height = 125
lc.data = data

# Category - Axis Horizontal
catNames = 'Jan Feb Mar Apr May Jun Jul Aug'.split(' ')
lc.categoryAxis.categoryNames = catNames
lc.categoryAxis.labels.boxAnchor = 'n'

# Values - Axis Vertical
lc.valueAxis.valueMin = 0
lc.valueAxis.valueMax = 60
lc.valueAxis.valueStep = 15

# Line Configuration
lc.joinedLines = 1
lc.lines[0].strokeWidth = 2.0
lc.lines[1].strokeWidth = 1.5

# Presentation
d.add(lc)
renderPDF.drawToFile(d=d, fn="graphic_line.pdf", msg="Graphic Line")
