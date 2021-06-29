from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4


def translate(canvas):
    canvas.translate(2*cm, 12*cm)


def scale(canvas):
    canvas.scale(1.2, 1.2)


lyrics = str('''well she hit Net Solutions
and she registered her own .com site now
and filled it up with yahoo profile pics
she snarfed in one night now
and she made 50 million when Hugh Hefner
bought up the rights now
and she'll have fun fun fun
til her Daddy takes the keyboard away''')

lyrics = lyrics.split("\n")


def charspace(canvas):
    textobject = canvas.beginText()
    textobject.setTextOrigin(4, 2.5*inch)
    textobject.setFont(psfontname="Helvetica-Oblique", size=12)
    char_space = 0

    for line in lyrics:
        textobject.setCharSpace(char_space)  # Espaçamento entre os caracteres
        textobject.textLine("%s: %s" % (char_space, line))
        char_space += 0.5

    textobject.setFillGray(gray=0.4)
    textobject.textLines('''
    With many apologies to the Beach Boys
    and anyone else who finds this objectionable
    ''')
    canvas.drawText(aTextObject=textobject)


if __name__ == '__main__':
    pdf = Canvas(filename="character_spacing.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    charspace(pdf)
    pdf.showPage()
    pdf.save()
