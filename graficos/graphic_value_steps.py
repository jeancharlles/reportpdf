from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.axes import XValueAxis
from reportlab.graphics import renderPDF


d = Drawing(400, 100)

data = [(10, 20, 30, 40)]

xAxis = XValueAxis()
xAxis.setPosition(75, 50, 300)
xAxis.valueSteps = [10, 15, 20, 30, 35, 40]
xAxis.configure(data)
xAxis.labels.boxAnchor = 'n'

d.add(xAxis)

renderPDF.drawToFile(d=d, fn="graphic_value_steps.pdf", msg="My Value Step")
