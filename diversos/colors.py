from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors
from reportlab.lib.units import inch, cm


def translate(canvas):
    canvas.translate(3.5*cm, 12*cm)


def colorsrgb(canvas):
    black = colors.black
    y = 0
    x = 0
    dy = 3*inch/4
    dx = 5.5*inch/5
    w = h = dy/2
    rdx = (dx-w)/2
    rdy = h/5
    texty = h + (2*rdy)

    canvas.setFont("Helvetica", 10)

    for [namedcolor, name] in ([colors.lavenderblush, "lavenderblush"], [colors.lawngreen, "lawngreen"],
                               [colors.lemonchiffon, "lemonchiffon"], [colors.lightblue, "lightblue"],
                               [colors.lightcoral, "lightcoral"]):
        canvas.setFillColor(namedcolor)
        canvas.rect(x+rdx, y+rdy, w, h, fill=1)
        canvas.setFillColor(black)
        canvas.drawCentredString(x + dx/2, y + texty, name)
        x += dx
    y += dy
    x = 0

    for rgb in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0.5, 0.3, 0.1), (0.4, 0.5, 0.3)]:
        r, g, b = rgb
        canvas.setFillColorRGB(r, g, b)
        canvas.rect(x+rdx, y+rdy, w, h, fill=1)
        canvas.setFillColor(black)
        canvas.drawCentredString(x+dx/2, y+texty, "r%s g%s b%s" % rgb)
        x = x + dx
    y += dy
    x = 0

    for gray in (0.0, 0.25, 0.50, 0.75, 1.0):
        canvas.setFillGray(gray)
        canvas.rect(x+rdx, y+rdy, w, h, fill=1)
        canvas.setFillColor(black)
        canvas.drawCentredString(x+dx/2, y+texty, "gray: %s" % gray)
        x += dx


if __name__ == '__main__':
    pdf = Canvas(filename="colors.pdf")
    translate(pdf)
    colorsrgb(pdf)
    pdf.showPage()
    pdf.save()
