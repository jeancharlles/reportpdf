from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_settings import defaultPageSize
from reportlab.lib.units import inch


PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIDTH = defaultPageSize[0]
styles = getSampleStyleSheet()

Title = "Hello World"
pageinfo = """platypus example"""


def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont(psfontname="Times-Bold", size=16)
    canvas.drawCentredString(PAGE_WIDTH, PAGE_HEIGHT, Title)
    canvas.setFont(psfontname="Times-Roman", size=9)
    canvas.drawString(inch, 0.75*inch, "First Page %s" % pageinfo)
    canvas.restoreState()


def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont(psfontname="Times-Roman", size=9)
    canvas.drawString(inch, 0.75*inch, "Page %d %s" % (doc.pageinfo, pageinfo))
    canvas.restoreState()


def go():
    doc = SimpleDocTemplate(filename="phello.pdf")
    story = [Spacer(1, 2*inch)]
    style = styles["Normal"]
    for i in range(100):
        bogustext = ("This is Paragraph number %s" % i) * 20
        p = Paragraph(bogustext, style)
        story.append(p)
        story.append(Spacer(1, 0.2*inch))

    doc.build(flowables=story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)


if __name__ == '__main__':
    go()
