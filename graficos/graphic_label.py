from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing, Circle
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib.colors import green


d = Drawing(width=200, height=100)

d.add(Circle(cx=100, cy=90, r=5, fillColor=green))

lab = Label()
lab.setOrigin(x=100, y=90)
lab.boxAnchor = 'ne'
lab.angle = 45
lab.dx = 0
lab.dy = -20
lab.boxStrokeColor = green
lab.setText(text="""
Some 
Multi-Line
Label""")
d.add(lab)

renderPDF.drawToFile(d=d, fn="graphic_label.pdf", msg="My Label",)
