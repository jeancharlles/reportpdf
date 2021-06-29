from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import pink, red, green, blue


def coords(c):
    c.setStrokeColor(pink)
    c.grid(xlist=[1*inch, 2*inch, 3*inch, 4*inch], ylist=[0.5*inch, 1*inch, 1.5*inch, 2*inch, 2.5*inch])
    c.setStrokeColor(blue)
    c.setFont(psfontname="Times-Roman", size=18)
    c.drawString(18, 10, text="(0, 0) the Origin")
    c.setFont(psfontname="Helvetica", size=16)
    c.drawString(2*inch, 1*inch, text="(2.5, 1) in inches")
    c.drawString(4*inch, 2.5*inch, text="(4, 2.5) in inches")

    c.setFillColor(red)
    c.rect(4.5*inch, 2*inch, 0.4*inch, 0.3*inch, fill=1)

    c.setFillColor(green)
    c.circle(4.5*inch, 1.5*inch, 0.3*inch, fill=1)


if __name__ == '__main__':
    pdf = Canvas(filename="coords.pdf")
    coords(pdf)
    pdf.showPage()
    pdf.save()
