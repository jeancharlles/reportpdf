from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
# from reportlab.lib.colors import green, pink, white, brown


"""
bookmarkPage(self, key,
                      fit="Fit",
                      left=None,
                      top=None,
                      bottom=None,
                      right=None,
                      zoom=None
                      )
"""


def bookmark(canvas, name):
    # canvas.bookmarkPage('my_bookmark', left=0, top=200)
    # canvas.bookmarkPage('my_bookmark', fit="XYZ", left=0, top=200, zoom=2)
    # canvas.bookmarkPage("Meaning_of_life")
    # canvas.linkAbsolute("Find the Meaning of Life", "Meaning_of_life", Rect=(inch, inch, 6*inch, 2*inch))
    canvas.linkAbsolute("Meaning_of_life", (inch, inch, 6 * inch, 2 * inch), Border='[0 0 0]')


if __name__ == '__main__':
    pdf = Canvas(filename="formulario2.pdf", pagesize=A4)
    bookmark(pdf, name="Meaning of Life")
    pdf.showPage()
    pdf.save()
