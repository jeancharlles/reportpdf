from reportlab.lib.colors import yellow
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import widgetbase
from reportlab.graphics import renderPDF

d = Drawing(width=200, height=100)

f = widgetbase.Face()
f.skinColor = yellow
# f.mood = "sad"
f.mood = "happy"


d.add(node=f, name='face')

renderPDF.drawToFile(d=d, fn="widgets_pdf.pdf", msg="A Face")
