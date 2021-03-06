from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib.colors import black
from reportlab.graphics import renderPDF

# Definition
d = Drawing(width=400, height=200)

# Data Series
data = [
    (13, 5, 20, 22, 37, 45, 19, 4),
    (14, 6, 21, 23, 38, 46, 20, 5),
    ]
# Type Chart
bc = VerticalBarChart()

# Property
bc.x = 50
bc.y = 50
bc.width = 300
bc.height = 125
bc.data = data
bc.strokeColor = black

# Axis Vertical - Value
bc.valueAxis.valueMin = 0
bc.valueAxis.valueMax = 50
bc.valueAxis.valueStep = 10

# Axis Horizontal - Category
bc.categoryAxis.labels.boxAnchor = 'ne'
bc.categoryAxis.labels.dx = 8
bc.categoryAxis.labels.dy = -2
bc.categoryAxis.labels.angle = 30
bc.categoryAxis.categoryNames = ['Jan-99', 'Feb-99', 'Mar-99', 'Apr-99', 'May-99', 'Jun-99', 'Jul-99', 'Aug-99']

# Spacing
bc.groupSpacing = 10
bc.barSpacing = 2.5

# Presentation
d.add(bc)
renderPDF.drawToFile(d=d, fn='graphic_bar_vertical.pdf', msg="Graphic Bar Vertical")
