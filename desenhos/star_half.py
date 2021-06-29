from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from math import pi, cos, sin


def translate(canvas):
    canvas.translate(2*cm, 12*cm)


def scale(canvas):
    canvas.scale(1.0, 1.0)


def star(canvas):
    nvertices = 4
    ycenter = 1.5*inch
    radius = 1*inch

    # Configuração para cada estrela
    for estrela in range(0, 3):
        if estrela == 1:
            title = "Default"
            aka = "no projection"
            xcenter = 1*inch
            modes = 0
        elif estrela == 2:
            title = "Round cap"
            aka = "1: ends in half circle"
            xcenter = 3.5*inch
            modes = 1
        else:
            title = "Square cap"
            aka = "2: projects out half a width"
            xcenter = 6*inch
            modes = 2

        # Texto e Comentário
        canvas.drawCentredString(x=xcenter, y=ycenter+1.4*radius, text=title)
        canvas.drawCentredString(x=xcenter, y=ycenter-1.4*radius, text=aka)

        # Largura e Borda da Linha
        canvas.setLineWidth(5)
        canvas.setLineJoin(mode=modes)
        canvas.setLineCap(mode=modes)

        p = canvas.beginPath()
        p.moveTo(xcenter, ycenter + radius)

        angle = (2*pi)*2/5.0
        startangle = pi/2.0

        for vertex in range(nvertices-1):
            nextangle = angle*(vertex + 1) + startangle
            x = xcenter + radius*cos(nextangle)
            y = ycenter + radius*sin(nextangle)
            p.lineTo(x, y)
            canvas.drawPath(p)

        if nvertices > 5:
            p.close()


if __name__ == '__main__':
    pdf = Canvas(filename="star_half.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    star(pdf)
    pdf.showPage()
    pdf.save()
