from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import CMYKColor, PCMYKColor


def translate(canvas):
    canvas.translate(2.5*cm, 12*cm)


def scale(canvas):
    canvas.scale(1.2, 1.2)


def colors_cmyk(canvas):

    # creates a black CMYK ; CMYKColor use real values
    black = CMYKColor(cyan=0, magenta=0, yellow=0, black=1)

    # Criado por mim
    # colores = CMYKColor(cyan=0.7, magenta=0.5, yellow=0.2, black=0.2)

    # creates a cyan CMYK ; PCMYKColor use integer values
    cyan = PCMYKColor(cyan=100, magenta=0, yellow=0, black=0)

    y = x = 0
    dy = inch * (3 / 4.0)
    dx = inch * (5.5 / 5)
    w = h = (dy / 2)
    rdx = (dx - w) / 2
    rdy = h / 5.0
    texty = h + 2 * rdy
    canvas.setFont("Helvetica", 10)
    y = y + dy

    for cmyk in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 0, 0)]:
        c, m, y1, k = cmyk
        canvas.setFillColorCMYK(c, m, y1, k)
        canvas.rect(x + rdx, y + rdy, w, h, fill=1)

        canvas.setFillColor(black)
        # canvas.setFillColor(colores)
        canvas.setStrokeColor(cyan)

        canvas.drawCentredString(x + dx / 2, y + texty, "c%s m%s y%s k%s" % cmyk)
        x += dx


if __name__ == '__main__':
    pdf = Canvas(filename="cmyk_colors.pdf")
    translate(pdf)
    scale(pdf)
    colors_cmyk(pdf)
    pdf.showPage()
    pdf.save()
