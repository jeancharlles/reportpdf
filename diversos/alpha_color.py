from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm
# from reportlab.graphics.shapes import Rect
from reportlab.lib.colors import Color, black, blue, red


def translate(canvas):
    canvas.translate(3.5*cm, 12*cm)


def alpha(canvas):
    red50transparent = Color(red=100, green=0, blue=0, alpha=0.5)
    blue50tranparent = Color(red=0, green=0, blue=100, alpha=0.5)

    c = canvas
    c.setFillColor(black)
    c.setFont(psfontname='Helvetica', size=10)
    c.drawString(x=25, y=180, text='solid')

    c.setFillColor(aColor=blue)
    c.rect(x=25, y=25, width=100, height=100, stroke=False, fill=True)

    c.setFillColor(aColor=red)
    c.rect(x=100, y=75, width=100, height=100, stroke=False, fill=True, )

    c.setFillColor(aColor=black)
    c.drawString(x=225, y=180, text='transparent')

    c.setFillColor(blue50tranparent)
    c.rect(x=225, y=25, width=100, height=100, fill=True, stroke=False)

    c.setFillColor(red50transparent)
    c.rect(x=300, y=75, width=100, height=100, fill=True, stroke=False)


if __name__ == '__main__':
    pdf = Canvas(filename="alpha_color.pdf")
    translate(pdf)
    alpha(pdf)
    pdf.showPage()
    pdf.save()
