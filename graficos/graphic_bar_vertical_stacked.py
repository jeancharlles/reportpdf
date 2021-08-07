from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib.colors import black

# Definition
d = Drawing(width=400, height=200)

# Data Series
data = [
    (10, 8, 7, 25, 42, 38, 41, 28),
    (12, 9, 12, 29, 44, 39, 43, 29),
]

# Type Chart
bc = VerticalBarChart()

# Property Graphic
bc.x = 50
bc.y = 50
bc.width = 300
bc.height = 125
bc.data = data
bc.strokeColor = black

# Axis Vertical
bc.valueAxis.valueMin = 0
bc.valueAxis.valueMax = 100
bc.valueAxis.valueStep = 10

# Axis Horizontal
bc.categoryAxis.labels.boxAnchor = 'ne'
bc.categoryAxis.labels.dx = 8
bc.categoryAxis.labels.dy = -2
bc.categoryAxis.labels.angle = 30
bc.categoryAxis.categoryNames = ['Jan-99', 'Feb-99', 'Mar-99', 'Apr-99', 'May-99', 'Jun-99', 'Jul-99', 'Aug-99']

# Spacing
bc.groupSpacing = 10
bc.barSpacing = 2.5

# Stack
bc.categoryAxis.style = 'stacked'

d.add(bc)
renderPDF.drawToFile(d=d, fn="graphic_bar_vertical_stacked.pdf", msg="Graphic Bar Vertical Stacked")
