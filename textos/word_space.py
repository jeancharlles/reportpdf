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


def wordspace(canvas):
    textobject = canvas.beginText()
    textobject.setTextOrigin(x=3, y=2.5*inch)
    textobject.setFont(psfontname="Helvetica-Oblique", size=12)
    word_space = 0

    for line in lyrics:
        textobject.setWordSpace(wordSpace=word_space)  # Espaçamento entre as palavras
        textobject.textLine("%s: %s" % (word_space, line))
        word_space += 2.5

    textobject.setFillColorCMYK(c=0.4, m=0, y=0.4, k=0.2)
    textobject.textLines(stuff='''
    With many apologies to the Beach Boys
    and anyone else who finds this objectionable
    ''')
    canvas.drawText(textobject)


if __name__ == '__main__':
    pdf = Canvas(filename='word_space.pdf', pagesize=A4)
    translate(pdf)
    scale(pdf)
    wordspace(pdf)
    pdf.showPage()
    pdf.save()
