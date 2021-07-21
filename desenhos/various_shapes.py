from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4


def translate(canvas):
    canvas.translate(dx=2*cm, dy=10*cm)


def scale(canvas):
    canvas.scale(x=1.2, y=1.2)


def variousshapes(canvas):
    # Configuração da polegada
    i = int(inch)
    canvas.setStrokeGray(0.5)  # Defina a cor cinza do grid
    canvas.grid(xlist=range(0, int(11*i/2), int(i/2)), ylist=range(0, int(7*i/2), int(i/2)))  # Define o grid

    # Configuração da Linha
    canvas.setLineWidth(width=4)
    canvas.setStrokeColorRGB(r=0, g=0.2, b=0.7)
    canvas.setFillColorRGB(r=1, g=0.6, b=0.8)

    # Desenho das 3 figuras geométricas
    p = canvas.beginPath()
    p.rect(x=0.5*inch, y=0.5*inch, width=0.5*inch, height=2*inch)
    p.circle(x_cen=2.75*inch, y_cen=1.5*inch, r=0.3*inch)
    p.ellipse(x=3.5*inch, y=0.5*inch, width=1.2*inch, height=2*inch)
    canvas.drawPath(p, fill=1, stroke=1)


if __name__ == '__main__':
    pdf = Canvas(filename="various_shapes.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    variousshapes(pdf)
    pdf.showPage()
    pdf.save()
