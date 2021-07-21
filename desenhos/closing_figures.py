from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4


def translate(canvas):
    canvas.translate(dx=5*cm, dy=10*cm)


def scale(canvas):
    canvas.scale(x=1.0, y=1.0)


def closingfigures(canvas):
    h = inch/3.0
    k = inch/2.0
    canvas.setStrokeColorRGB(r=0.2, g=0.3, b=0.5)
    canvas.setFillColorRGB(r=0.8, g=0.6, b=0.2)
    canvas.setLineWidth(4)

    p = canvas.beginPath()

    for i in (1, 2, 3, 4):

        for j in (1, 2):
            xc, yc = inch*i, inch*j
            p.moveTo(xc, yc)
            p.arcTo(xc-h, yc-k, xc+h, yc+k, startAng=0, extent=60*i)

            # close only the first one, not the second one
            if j == 1:
                p.close()
    canvas.drawPath(p, fill=1, stroke=1)


if __name__ == '__main__':
    pdf = Canvas(filename="closing_figures.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    closingfigures(pdf)
    pdf.showPage()
    pdf.save()
