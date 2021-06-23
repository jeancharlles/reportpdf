from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4


def translate(canvas):
    canvas.translate(2*cm, 7*cm)


def scale(canvas):
    canvas.scale(1.2, 1.2)


def fonts(canvas):
    canvas.setFont(psfontname="Helvetica-Bold", size=10)
    canvas.drawString(x=1.8*inch, y=3*inch, text="Exemplos de Fonts")
    text = "Now is the time for all good men to..."
    x = 1.8*inch
    y = 2.7*inch
    for font in canvas.getAvailableFonts():
        canvas.setFont(psfontname=font, size=10)
        canvas.drawString(x=x, y=y, text=text)
        canvas.setFont(psfontname="Helvetica", size=10)
        canvas.drawRightString(x=x-10, y=y, text=font+":")
        y = y-13


if __name__ == '__main__':
    pdf = Canvas(filename="fonts_examples.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    fonts(pdf)
    pdf.showPage()
    pdf.save()
