from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.colors import red

# Definition
d = Drawing(width=200, height=100)
data = [10, 20, 30, 40, 50, 60]
label = ['a', 'b', 'c', 'd', 'e', 'f']

# Type Chart
pc = Pie()

# Property
pc.x = 65
pc.y = 15
pc.width = 70
pc.height = 70
pc.data = data
pc.labels = label

# Configuration Universals of Slices
pc.slices.strokeWidth = 0.5
pc.slices.fontName = 'Helvetica'
pc.slices.fontSize = 10

# Configuration of specify Slice
pc.slices[3].popout = 5
pc.slices[3].strokeWidth = 1
pc.slices[3].strokeDashArray = [1, 1]
pc.slices[3].labelRadius = 1.25
pc.slices[3].fontColor = red

# Presentation
d.add(pc)
renderPDF.drawToFile(d=d, fn="graphicpie.pdf", msg="Graphic Pie")
