from reportlab.graphics.shapes import String, Drawing
from reportlab.graphics import renderPDF

d = Drawing(width=400, height=200)

for size in range(12, 36, 4):
    d.add(node=String(
        x=10+size*2,
        y=10+size*2,
        text='Hello World',
        fontName='Times-Roman',
        fontSize=size),
        name='string1')

d.add(node=String(
    x=130,
    y=120,
    text='Hello World',
    fontName='Courier',
    fontSize=36),
    name='string2')

d.add(node=String(
    x=150,
    y=160,
    text='Hello World',
    fontName='DarkGardenMK',
    fontSize=36),
    name='string3')

renderPDF.drawToFile(d=d, fn="shapes_strings.pdf", msg="Strings")
