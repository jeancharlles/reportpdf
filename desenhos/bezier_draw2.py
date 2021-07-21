from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import green, red, black
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4


def translate(canvas):
    canvas.translate(dx=5*cm, dy=10*cm)


def scale(canvas):
    canvas.scale(x=1.0, y=1.0)


def bezier2(canvas):
    #  make a sequence of control points
    xd, yd = 5.5*inch/2, 3*inch/2
    xc, yc = xd, yd

    dxdy = [(0, 0.33), (0.33, 0.33), (0.75, 1), (0.875, 0.875), (0.875, 0.875), (1, 0.75), (0.33, 0.33), (0.33, 0)]
    pointlist = []

    for xoffset in (1, -1):
        yoffset = xoffset

        for (dx, dy) in dxdy:
            px = xc + (xd * xoffset * dx)
            py = yc + (yd * yoffset * dy)
            pointlist.append((px, py))
        yoffset = -xoffset

        for (dy, dx) in dxdy:
            px = xc + xd * xoffset * dx
            py = yc + yd*yoffset*dy
            pointlist.append((px, py))

        # draw tangent lines and curves
    canvas.setLineWidth(inch*0.1)

    while pointlist:
        [(x1, y1), (x2, y2), (x3, y3), (x4, y4)] = pointlist[:4]
        del pointlist[:4]

        canvas.setLineWidth(inch*0.1)
        canvas.setStrokeColor(green)
        canvas.line(x1, y1, x2, y2)

        canvas.setStrokeColor(red)
        canvas.line(x3, y3, x4, y4)

        # finally draw the curve
        canvas.setStrokeColor(black)
        canvas.bezier(x1, y1, x2, y2, x3, y3, x4, y4)


if __name__ == '__main__':
    pdf = Canvas(filename="bezier_draw2.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    bezier2(pdf)
    pdf.showPage()
    pdf.save()
