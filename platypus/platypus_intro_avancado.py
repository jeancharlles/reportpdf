from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
import io
from django.http import FileResponse
from reportlab.pdfgen.canvas import Canvas


styles = getSampleStyleSheet()

Title = "Hello World"
pageinfo = "Página"


def myfirstpage(canvas, doc):
    canvas.saveState()
    canvas.setFont(psfontname="Times-Bold", size=16)
    canvas.drawCentredString(x=3*inch, y=10*inch, text=Title)
    canvas.setFont(psfontname="Times-Roman", size=9)
    canvas.drawString(x=1*inch, y=0.75*inch, text="Introdução")
    canvas.restoreState()


def mylaterpages(canvas, doc):
    canvas.saveState()
    canvas.setFont(psfontname="Times-Roman", size=9)
    canvas.drawString(x=1*inch, y=0.75*inch, text=pageinfo)
    canvas.drawString(x=1.5*inch, y=0.75*inch, text=str(canvas.getPageNumber()))
    canvas.restoreState()


def go():
    buffer = io.BytesIO()
    pdf = Canvas(buffer, pagesize=A4)
    doc = SimpleDocTemplate(filename="platypus_intro2.pdf", pagesize=A4, title="Lista")
    story = [Spacer(1, 2*inch)]
    style = styles["Normal"]
    for i in range(20):
        bogustext = ("This is Paragraph number %s " % i) * 10
        paragrafo = Paragraph(bogustext, style)
        story.append(paragrafo)
        story.append(Spacer(width=1, height=0.2*inch))

    doc.build(flowables=story, onFirstPage=myfirstpage, onLaterPages=mylaterpages)
    text_object = pdf.beginText()
    text_object.setTextOrigin(x=2*inch, y=2*inch)
    pdf.drawText(aTextObject=doc)
    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=False, filename='platypus_intro_avancado.pdf')


if __name__ == '__main__':
    go()
