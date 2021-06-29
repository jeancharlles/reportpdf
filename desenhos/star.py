from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from math import pi, cos, sin


def translate(canvas):
    canvas.translate(2*cm, 12*cm)


def scale(canvas):
    canvas.scale(1.2, 1.2)


def star(canvas):
    title = "Title Here"
    aka = "Comment here."
    nvertices = 5
    radius = 1*inch
    xcenter = 2.75*inch
    ycenter = 1.5*inch

    canvas.drawCentredString(x=xcenter, y=ycenter+1.3*radius, text=title)
    canvas.drawCentredString(x=xcenter, y=ycenter-1.4*radius, text=aka)
    p = canvas.beginPath()
    p.moveTo(xcenter, ycenter + radius)

    angle = (2*pi)*2/5.0
    startangle = pi/2.0

    for vertex in range(nvertices):
        nextangle = angle*(vertex + 1) + startangle
        x = xcenter + radius*cos(nextangle)
        y = ycenter + radius*sin(nextangle)
        p.lineTo(x, y)
        canvas.drawPath(p)

    if nvertices > 5:
        p.close()


if __name__ == '__main__':
    pdf = Canvas(filename="star.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    star(pdf)
    pdf.showPage()
    pdf.save()
