from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch


def charspace(canvas):
    lyrics = """well she hit Net Solutions
    and she registered her own .com site now
    and filled it up with yahoo profile pics
    she snarfed in one night now
    and she made 50 million when Hugh Hefner
    bought up the rights now
    and she'll have fun fun fun
    til her Daddy takes the keyboard away"""
    textobject = canvas.beginText()
    textobject.setTextOrigin(3, 2.5*inch)
    textobject.setFont("Helvetica-Oblique", 10)
    char_space = 0
    for line in lyrics:
        textobject.setCharSpace(char_space)
        textobject.textLine("%s: %s" % (char_space, line))
        char_space = char_space+0.5
    textobject.setFillGray(0.4)
    textobject.textLines('''
    With many apologies to the Beach Boys
    and anyone else who finds this objectionable
    ''')
    canvas.drawText(textobject)


if __name__ == '__main__':
    pdf = Canvas(filename="text_object_methods3.pdf", bottomup=1)
    charspace(pdf)
    pdf.showPage()
    pdf.save()
