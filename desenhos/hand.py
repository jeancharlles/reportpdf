from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import red, green


def translate(canvas):
    canvas.translate(dx=5*cm, dy=10*cm)


def scale(canvas):
    canvas.scale(x=1.0, y=1.0)


def hand(canvas, debug=1, fill=0):
    (startx, starty) = (0, 0)
    curves = [
        (0, 2), (0, 4), (0, 8),  # back of hand
        (5, 8), (7, 10), (7, 14),
        (10, 14), (10, 13), (7.5, 8),  # thumb
        (13, 8), (14, 8), (17, 8),
        (19, 8), (19, 6), (17, 6),
        (15, 6), (13, 6), (11, 6),  # index, pointing
        (12, 6), (13, 6), (14, 6),
        (16, 6), (16, 4), (14, 4),
        (13, 4), (12, 4), (11, 4),  # middle
        (11.5, 4), (12, 4), (13, 4),
        (15, 4), (15, 2), (13, 2),
        (12.5, 2), (11.5, 2), (11, 2),  # ring
        (11.5, 2), (12, 2), (12.5, 2),
        (14, 2), (14, 0), (12.5, 0),
        (10, 0), (8, 0), (6, 0),  # pinky, then close
    ]

    if debug:
        canvas.setLineWidth(6)
    u = inch*0.2
    p = canvas.beginPath()
    p.moveTo(startx, starty)
    ccopy = list(curves)

    while ccopy:
        [(x1, y1), (x2, y2), (x3, y3)] = ccopy[:3]
        del ccopy[:3]
        p.curveTo(x1*u, y1*u, x2*u, y2*u, x3*u, y3*u)

    p.close()
    canvas.drawPath(p, fill=fill)

    if debug:
        (lastx, lasty) = (startx, starty)
        ccopy = list(curves)
        while ccopy:
            [(x1, y1), (x2, y2), (x3, y3)] = ccopy[:3]
            del ccopy[:3]
            canvas.setStrokeColor(red)
            canvas.line(lastx*u, lasty*u, x1*u, y1*u)
            canvas.setStrokeColor(green)
            canvas.line(x2*u, y2*u, x3*u, y3*u)
            (lastx, lasty) = (x3, y3)


if __name__ == '__main__':
    pdf = Canvas(filename="hand.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    hand(pdf)
    pdf.showPage()
    pdf.save()
