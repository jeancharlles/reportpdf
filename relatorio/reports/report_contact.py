from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
# from relatorio.models import Contact
import os

pastaApp = os.path.dirname(__file__)


def translate(canvas):
    canvas.translate(0.5*cm, 12*cm)


def scale(canvas):
    canvas.scale(1.2, 1.2)


def cursormoves1(canvas):
    """Returns a fresh text object.  Text objects are used
       to add large amounts of text.  See PDFTextObject
       Coloque dentro de colchetes o texto []"""

    lyrics = ["""well she hit Net Solutions
    and she registered her own .com site now
    and filled it up with yahoo profile pics
    she snarfed in one night now
    and she made 50 million when Hugh Hefner
    bought up the rights now
    and she'll have fun fun fun
    til her Daddy takes the keyboard away
    """]

    # lyrics = Contact()

    textobject = canvas.beginText()  # Variável onde vai iniciar o texto
    textobject.setTextOrigin(x=1*inch, y=2.5*inch)  # Posicionamento inicial do texto
    textobject.setFont(psfontname="Helvetica-Oblique", size=14)  # Configurar a fonte e o tamanho do texto
    # for line in lyrics.first_name.all():
    #     textobject.textLines(stuff=line, trim=1)
    textobject.setFillGray(gray=0.4)
    textobject.textLines(stuff='''    
        With many apologies to the Beach Boys
        and anyone else who finds this objectionable
        ''', trim=1)
    canvas.drawText(aTextObject=textobject)


def criarpdf(request):
    request.drawString(x=100, y=100, text="Teste")


if __name__ == '__main__':
    pdf2 = Canvas(filename=pastaApp + "\\report_contact.pdf", pagesize=A4)
    pdf = Canvas(filename="report_contact.pdf", pagesize=A4)

    translate(pdf)
    scale(pdf)
    criarpdf(pdf2)
    cursormoves1(pdf)
    pdf2.showPage()
    pdf2.save()
