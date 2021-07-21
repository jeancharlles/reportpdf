from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4


def translate(canvas):
    canvas.translate(dx=5*cm, dy=10*cm)


def scale(canvas):
    canvas.scale(x=1.2, y=1.2)


def arcs(canvas):
    canvas.setLineWidth(4)
    canvas.setStrokeColorRGB(0.8, 1, 0.6)

    # draw rectangles enclosing the arcs
    canvas.rect(x=inch, y=inch, width=1.5*inch, height=inch)
    canvas.rect(x=3*inch, y=inch, width=inch, height=1.5*inch)
    canvas.setStrokeColorRGB(r=0, g=0.2, b=0.4)
    canvas.setFillColorRGB(r=1, g=0.6, b=0.8)

    p = canvas.beginPath()  # Início do Caminho do Objeto
    p.moveTo(x=0.2*inch, y=0.2*inch)
    p.arcTo(x1=1*inch, y1=1*inch, x2=2.5*inch, y2=2*inch, startAng=-30, extent=135)
    p.arc(x1=3*inch, y1=1*inch, x2=4*inch, y2=2.5*inch, startAng=-45, extent=270)
    canvas.drawPath(p, fill=1, stroke=1)  # Desenha o Caminho do Objeto com as informações acima


if __name__ == '__main__':
    pdf = Canvas(filename="arcs.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    arcs(pdf)
    pdf.showPage()
    pdf.save()
