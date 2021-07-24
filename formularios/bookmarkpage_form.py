from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm


def translate(canvas):
    canvas.translate(dx=2*cm, dy=10*cm)


def scale(canvas):
    canvas.scale(x=1.2, y=1.2)


def bookmark(canvas):

    # Bookmark 1
    canvas.drawCentredString(x=50, y=300, text="Page 1")
    canvas.bookmarkPage(key="page1", fit="FitH")
    canvas.addOutlineEntry(title="page 1", key="page1", level=0, closed=1)
    canvas.showPage()

    canvas.drawCentredString(x=150, y=350, text="Nível 1 da página 1")
    canvas.bookmarkPage(key="page1-l1", fit="FitV")
    canvas.addOutlineEntry(title="nível A", key="page1-l1", level=1, closed=0)
    canvas.showPage()

    # Bookmark 2
    canvas.drawCentredString(x=100, y=500, text="Page 2")
    canvas.bookmarkPage(key="page2", fit="XYZ", left=0, top=600, zoom=2)
    canvas.addOutlineEntry(title="page 2", key="page2", level=0)
    canvas.showPage()

    canvas.drawCentredString(x=150, y=350, text="Nível 1 da página 2")
    canvas.bookmarkPage(key="page2-l1", fit="FitV")
    canvas.addOutlineEntry(title="nivel B", key="page2-l1", level=1)
    canvas.showPage()

    canvas.save()


if __name__ == '__main__':
    pdf = Canvas(filename="bookmarkpage_form.pdf", pagesize=A4)
    translate(pdf)
    scale(pdf)
    bookmark(pdf)
