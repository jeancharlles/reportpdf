from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.axes import XCategoryAxis, YValueAxis
from reportlab.graphics import renderPDF

# Definition
d = Drawing(width=400, height=200)

# Data Series
data = [
    (10, 20, 30, 40),
    (15, 22, 37, 42)
]

# Eixo X
xAxis = XCategoryAxis()
xAxis.setPosition(x=75, y=75, length=300)
xAxis.configure(multiSeries=data)
xAxis.categoryNames = ['Beer', 'Wine', 'Meat', 'Cannelloni']
xAxis.labels.boxAnchor = 'n'
xAxis.labels[3].dy = -15
xAxis.labels[3].angle = 30
xAxis.labels[3].fontName = 'Times-Bold'

# Eixo Y
yAxis = YValueAxis()
yAxis.setPosition(x=50, y=50, length=125)
yAxis.configure(dataSeries=data)
yAxis.scale(value=40)

# Presentation
d.add(xAxis)
d.add(yAxis)

renderPDF.drawToFile(d=d, fn="graphic_axes.pdf", msg="My Axes")


# >>> yAxis = YValueAxis()
# >>> yAxis.setPosition(50, 50, 125)
# >>> data = [(10, 20, 30, 40),(15, 22, 37, 42)]
# >>> yAxis.configure(data)
# >>> yAxis.scale(10) # should be bottom of chart
# 50.0
# >>> yAxis.scale(40) # should be near the top
# 167.1875
# >>>
