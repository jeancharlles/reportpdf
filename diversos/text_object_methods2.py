from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4


def translate(canvas):
    canvas.translate(0.5*cm, 12*cm)


def scale(canvas):
    canvas.scale(1.2, 1.2)


lyrics = str('''
well she hit Net Solutions
and she registered her own .com site now
and filled it up with yahoo profile pics
she snarfed in one night now
and she made 50 million when Hugh Hefner
bought up the rights now
and she'll have fun fun fun
til her Daddy takes the keyboard away''')


lyrics = lyrics.split("\n")


def cursormoves2(canvas):
    textobject = canvas.beginText()
    textobject.setTextOrigin(2, 2.5*inch)
    textobject.setFont("Helvetica-Oblique", 14)
    for line in lyrics:
        textobject.textOut(line)
        textobject.moveCursor(14, 14)  # POSITIVE Y moves down!!!
    textobject.setFillColorRGB(0.4, 0, 1)
    textobject.textLines('''
    With many apologies to the Beach Boys
    and anyone else who finds this objectionable
    ''')
    canvas.drawText(textobject)


if __name__ == '__main__':
    pdf = Canvas(filename="text_object_methods2.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    cursormoves2(pdf)
    pdf.showPage()
    pdf.save()
