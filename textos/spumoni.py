from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import pink, green, brown, white


def translate(canvas):
    canvas.translate(2*cm, 7*cm)


def scale(canvas):
    canvas.scale(1.2, 1.2)


def spumoni(canvas):
    x = 0
    dx = 0.4*inch
    for i in range(4):
        for color in (pink, green, brown):
            canvas.setFillColor(color)
            canvas.rect(x, 0, dx, 3*inch, stroke=0, fill=1)
            x = x+dx
    canvas.setFillColor(white)
    canvas.setStrokeColor(white)
    canvas.setFont("Helvetica-Bold", 85)
    canvas.drawCentredString(x=2.75*inch, y=1.3*inch, text="SPUMONI")


if __name__ == '__main__':
    pdf = Canvas(filename='spumoni.pdf')
    translate(pdf)
    scale(pdf)
    spumoni(pdf)
    pdf.showPage()
    pdf.save()
