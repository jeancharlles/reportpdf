from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import pink, red, green, blue, black


def scaletranslate(canvas):
    canvas.setFont("Courier-BoldOblique", 12)

    # save the state
    canvas.saveState()

    # scale then translate
    canvas.scale(0.5, 0.5)
    canvas.translate(3*inch, 1.5*inch)
    canvas.drawString(0, 2.7*inch, "Scale then translate")
    coords(canvas)

    # forget the scale and translate
    canvas.restoreState()

    # translate then scale
    canvas.translate(4*inch, 1.5*inch)
    canvas.scale(0.5, 0.5)
    canvas.drawString(0, 2.7*inch, "Translate then scale")
    coords(canvas)


def coords(c):
    c.setStrokeColor(pink)
    c.grid(xlist=[1*inch, 2*inch, 3*inch, 4*inch],
           ylist=[0.5*inch, 1*inch, 1.5*inch, 2*inch, 2.5*inch])
    c.setStrokeColor(blue)
    c.setFont(psfontname="Times-Roman", size=18)
    c.drawString(18, 10, text="(0, 0) the Origin")
    c.setFont(psfontname="Helvetica", size=16)
    c.drawString(2*inch, 1*inch, text="(2, 1) in inches")
    c.drawString(4*inch, 2.5*inch, text="(4, 2.5) in inches")

    c.setFillColor(red)
    c.rect(0.5*inch, 2*inch, 0.4*inch, 0.3*inch, fill=1)

    c.setFillColor(black)
    c.drawString(1*inch, 2*inch, text="(1, 2) in inches")

    c.setFillColor(green)
    c.circle(4.5*inch, 1.5*inch, 0.3*inch, fill=1)


if __name__ == '__main__':
    pdf = Canvas(filename="scaletranslate.pdf")
    scaletranslate(pdf)
    pdf.showPage()
    pdf.save()
