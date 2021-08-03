from reportlab.lib.colors import yellow, red
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.graphics import renderPDF


d = Drawing(width=400, height=200)
d.add(Rect(x=50, y=50, width=300, height=100, fillColor=yellow))
d.add(String(x=150, y=100, text="Hello World", fontSize=18, fillColor=red))
d.add(String(x=180, y=86,
             text="Special characters \xc2\xa2\xc2\xa9\xc2\xae\xc2\xa3\xce\xb1\xce\xb2",
             fillColor=red
             )
      )

renderPDF.drawToFile(d=d, fn="first_graphic.pdf", msg="My first Drawing")
