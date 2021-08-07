from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.colors import black

# Definition
d = Drawing(width=400, height=200)
data = [
    ((1, 1), (2, 2), (2.5, 1), (3, 3), (4, 5)),
    ((1, 2), (2, 3), (2.5, 2), (3, 4), (4, 6))
]

# Type Chart
lp = LinePlot()

# Property
lp.x = 50
lp.y = 40
lp.height = 125
lp.width = 300
lp.data = data
lp.strokeColor = black

# Line Configuration
lp.joinedLines = 1  # 0 - Mostra apenas os valores
lp.lines[0].symbol = makeMarker(name='FilledCircle')
lp.lines[1].symbol = makeMarker(name='Circle')
lp.lineLabelFormat = '%2.0f'


# Category - Axis Horizontal - X
lp.xValueAxis.valueMin = 0
lp.xValueAxis.valueMax = 5
lp.xValueAxis.valueSteps = [1, 2, 2.5, 3, 4, 5]
lp.xValueAxis.labelTextFormat = '%2.1f'

# Values - Axis Vertical - Y
lp.yValueAxis.valueMin = 0
lp.yValueAxis.valueMax = 7
lp.yValueAxis.valueSteps = [1, 2, 3, 4, 5, 6]

# Presentation
d.add(lp)
renderPDF.drawToFile(d=d, fn="graphic_line_plot.pdf", msg="Graphic Line Plot")
