from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import green, pink, white, brown


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


def forms(canvas):
    # first create a form...
    canvas.beginForm("SpumoniForm")
    spumoni(canvas)
    canvas.endForm()

    # then draw it
    canvas.doForm("SpumoniForm")


if __name__ == '__main__':
    pdf = Canvas(filename="formulario1.pdf", pagesize=A4)
    # bookmark(pdf)
    forms(pdf)
    pdf.showPage()
    pdf.save()
