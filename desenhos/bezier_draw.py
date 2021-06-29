from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import yellow, green, red, black
from reportlab.lib.pagesizes import A4


def translate(canvas):
    canvas.translate(dx=5*cm, dy=10*cm)


def scale(canvas):
    canvas.scale(x=1.0, y=1.0)


def bezier(canvas):
    i = 1*inch
    d = i/4

    # define the bezier curve control points
    x1, y1, x2, y2, x3, y3, x4, y4 = d, 1.5*i, 1.5*i, d, 3*i, d, 5.5*i-d, 3*i-d

    # Desenha Amarelo
    canvas.setFillColor(aColor=yellow)
    p = canvas.beginPath()
    p.moveTo(x=x1, y=y1)
    for (x, y) in [(x2, y2), (x3, y3), (x4, y4)]:
        p.lineTo(x=x, y=y)
    canvas.drawPath(aPath=p, stroke=0, fill=1)

    #  Largura das linhas
    canvas.setLineWidth(width=0.1*i)

    # Desenho da Linha Verde
    canvas.setStrokeColor(aColor=green)
    canvas.line(x1=x1, y1=y1, x2=x2, y2=y2)

    # Desenho da Linha Vermelha
    canvas.setStrokeColor(aColor=red)
    canvas.line(x1=x3, y1=y3, x2=x4, y2=y4)

    # Desenho Bezier Preto
    canvas.setStrokeColor(aColor=black)
    canvas.bezier(x1, y1, x2, y2, x3, y3, x4, y4)


if __name__ == "__main__":
    pdf = Canvas(filename="bezier_draw.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    bezier(pdf)
    pdf.showPage()
    pdf.save()
