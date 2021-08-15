from reportlab.graphics.shapes import Rect, Drawing
from reportlab.lib.colors import red, green
from reportlab.graphics import renderPDF


d = Drawing(width=800, height=400)

r = Rect(x=100, y=150, width=200, height=100)
r.fillColor = red
r.strokeColor = green
r.strokeWidth = 3

d.add(r, 'Rect')

renderPDF.drawToFile(d=d, fn="shapes_report.pdf", msg="Rect")
