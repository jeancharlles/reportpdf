from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from math import pi, cos, sin


def translate(canvas):
    canvas.translate(2*cm, 12*cm)


def scale(canvas):
    canvas.scale(1.0, 1.0)


def star_dashes(canvas):
    nvertices = 5
    ycenter = 1.5*inch
    radius = 1*inch

    # Configuração para cada estrela
    for estrela in range(0, 3):
        if estrela == 1:
            title = "Simple dashes"
            aka = "6 points on, 3 off"
            xcenter = 1*inch
            # canvas.setDash(6, 3)
            canvas.setDash(array=[6, 3])
            modes = 0
        elif estrela == 2:
            title = "Round cap"
            aka = "1: ends in half circle"
            xcenter = 3.5*inch
            # canvas.setDash([1, 2])
            canvas.setDash(array=[1, 2])
            modes = 1
        else:
            title = "Square cap"
            aka = "2: projects out half a width"
            xcenter = 6*inch
            # canvas.setDash([1, 1, 3, 3, 1, 4, 4, 1])
            canvas.setDash(array=[1, 1, 3, 3, 1, 4, 4, 1])
            modes = 2

        # Texto e Comentário
        canvas.drawCentredString(x=xcenter, y=ycenter + 1.4 * radius, text=title)
        canvas.drawCentredString(x=xcenter, y=ycenter - 1.4 * radius, text=aka)

        # Largura e Borda da Linha
        canvas.setLineWidth(1)
        canvas.setLineJoin(mode=modes)
        canvas.setLineCap(mode=modes)

        p = canvas.beginPath()
        p.moveTo(xcenter, ycenter + radius)

        angle = (2*pi)*2 / 5.0
        startangle = pi/2.0

        for vertex in range(nvertices):
            nextangle = angle*(vertex + 1) + startangle
            x = xcenter + radius * cos(nextangle)
            y = ycenter + radius * sin(nextangle)
            p.lineTo(x, y)
            canvas.drawPath(p)

        if nvertices > 5:
            p.close()


if __name__ == '__main__':
    pdf = Canvas(filename="star_dash.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    star_dashes(pdf)
    pdf.showPage()
    pdf.save()
