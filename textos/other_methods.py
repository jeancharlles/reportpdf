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
rise = 0
mode = 0


def other_methods(canvas):
    textobject = canvas.beginText()
    textobject.setTextOrigin(x=2, y=3*inch)
    textobject.setFont(psfontname="Helvetica", size=14)

    varrise = 0
    modes = 0
    for line in lyrics:
        textobject.setTextRenderMode(mode=modes)  # possíveis 0, 1, 2, 3, 4, 5, 6, 7
        textobject.setRise(rise=varrise)
        textobject.textLine(f'mode={modes} rise={varrise} : {line}')
        if varrise == 0:
            varrise += 1
        else:
            varrise -= 1
        modes += 1
    textobject.textLines(stuff=lyrics)
    canvas.drawText(aTextObject=textobject)


if __name__ == '__main__':
    pdf = Canvas(filename='other_methods.pdf', pagesize=A4)
    translate(pdf)
    scale(pdf)
    other_methods(pdf)
    pdf.showPage()
    pdf.save()
