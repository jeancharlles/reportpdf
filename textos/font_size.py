from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import magenta, red


def textsize(canvas):
    # título
    canvas.setFont(psfontname="Times-Roman", size=20)
    canvas.setFillColor(red)
    canvas.drawCentredString(x=2.75*inch, y=2.5*inch, text="Font size examples")

    # Font size examples
    canvas.setFillColor(magenta)
    size = 7
    x = 1.3 * inch
    y = 2.3*inch

    lyrics = ['This is first line', 'This is second line', 'This is third line', 'This is the fourth line',
              'This is the fifth line', 'This is the sixth line', 'This is the seventh line']

    for line in lyrics:
        canvas.setFont("Helvetica", size)
        # Draws a string right-aligned with the x coordinate
        canvas.drawRightString(x=x, y=y, text="%s points: " % size)
        canvas.drawString(x, y, line)
        y = y - size*1.2
        size = size + 1.5


if __name__ == '__main__':
    pdf = Canvas(filename="font_size.pdf", pagesize=A4)
    textsize(pdf)
    pdf.showPage()
    pdf.save()
