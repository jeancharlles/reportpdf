from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import pink, green, brown, white, black


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


def spumoni2(canvas):
    # draw the previous drawing
    # now put an ice cream cone on top of it:

    # first draw a triangle (ice cream cone)
    p = canvas.beginPath()
    xcenter = 2.75*inch
    radius = 0.45*inch
    p.moveTo(xcenter-radius, 1.5*inch)
    p.lineTo(xcenter+radius, 1.5*inch)
    p.lineTo(xcenter, 0)
    canvas.setFillColor(brown)
    canvas.setStrokeColor(black)
    canvas.drawPath(p, fill=1)

    # draw some circles (scoops)
    y = 1.5*inch
    for color in (pink, green, brown):
        canvas.setFillColor(color)
        canvas.circle(xcenter, y, radius, fill=1)
        y = y+radius


if __name__ == '__main__':
    pdf = Canvas(filename='spumoni2.pdf')
    translate(pdf)
    scale(pdf)
    spumoni(pdf)
    spumoni2(pdf)
    pdf.showPage()
    pdf.save()
