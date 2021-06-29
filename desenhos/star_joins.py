from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from math import pi, cos, sin


def translate(canvas):
    canvas.translate(2*cm, 12*cm)


def scale(canvas):
    canvas.scale(1.0, 1.0)


def star(canvas):
    nvertices = 5
    ycenter = 1.5 * inch
    radius = 1 * inch

    for estrela in range(0, 3):
        if estrela == 1:
            title = "Default: mitered join"
            aka = "0: pointed"
            xcenter = 1*inch
            modes = 0
        elif estrela == 2:
            title = "Round join"
            aka = "1: rounded"
            xcenter = 3.5*inch
            modes = 1
        else:
            title = "Bevelled join"
            aka = "2: square"
            xcenter = 6*inch
            modes = 2

        canvas.drawCentredString(x=xcenter, y=ycenter+1.4*radius, text=title)
        canvas.drawCentredString(x=xcenter, y=ycenter-1.4*radius, text=aka)

        canvas.setLineWidth(5)
        canvas.setLineJoin(mode=modes)
        canvas.setLineCap(mode=modes)

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
    pdf = Canvas(filename="star_joins.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    star(pdf)
    pdf.showPage()
    pdf.save()
