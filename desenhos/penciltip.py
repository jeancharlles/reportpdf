from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import tan, black, green


def translate(canvas):
    canvas.translate(dx=5*cm, dy=12*cm)


def scale(canvas):
    canvas.scale(x=1.0, y=1.0)


def pencitltip(canvas, debug):
    u = 1*inch/10.0
    canvas.setLineWidth(width=4)
    if debug is True:
        canvas.scale(x=2.8, y=2.8)
        canvas.setLineWidth(width=1)

    # Desenho do Lápis
    canvas.setStrokeColor(aColor=black)  # Cor do traço
    canvas.setFillColor(aColor=tan)  # cor do preenchimento
    p = canvas.beginPath()  # Inicia caminho do desenho
    p.moveTo(x=10*u, y=0)  # Posiciona o início
    p.lineTo(x=0, y=5*u)  # Desenhe uma linha até a coordenada x, y
    p.lineTo(x=10*u, y=10*u)  # Desenha a linha até a coordenada x, y
    p.curveTo(x1=11.5*u, y1=10*u, x2=11.5*u, y2=7.5*u, x3=10*u, y3=7.5*u)  # desenhe uma curva até
    p.curveTo(x1=12.0*u, y1=7.5*u, x2=11*u, y2=2.5*u, x3=9.7*u, y3=2.5*u)
    p.curveTo(x1=10.5*u, y1=2.5*u, x2=11*u, y2=0*u, x3=10*u, y3=0*u)
    canvas.drawPath(aPath=p, stroke=1, fill=1)  # Desenha o caminho feito por p, com traço e preenchimento

    canvas.setFillColor(black)
    p = canvas.beginPath()
    p.moveTo(x=0, y=5*u)
    p.lineTo(x=4*u, y=3*u)
    p.lineTo(x=5*u, y=4.5*u)
    p.lineTo(x=3*u, y=6.5*u)
    canvas.drawPath(aPath=p, stroke=1, fill=1)  # Desenha o caminho feito por p, com traço e preenchimento

    if debug is True:
        canvas.setStrokeColor(aColor=green)
        canvas.grid(xlist=[0, 5*u, 10*u, 15*u], ylist=[0, 5*u, 10*u])


if __name__ == "__main__":
    pdf = Canvas(filename="penciltip.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    pencitltip(pdf, debug=True)
    pdf.showPage()
    pdf.save()
