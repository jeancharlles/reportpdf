from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch


def annotations(canvas):
    canvas.drawString(inch, 2.5*inch, "setAuthor, setTitle, setSubject have no visible effect")
    canvas.drawString(inch, inch, "But if you are viewing this document dynamically")
    canvas.drawString(inch, 0.5*inch, "please look at File/Document Info")
    canvas.setAuthor(author="the ReportLab Team")
    canvas.setTitle(title="ReportLab PDF Generation User Guide")
    canvas.setSubject(subject="How to Generate PDF files using the ReportLab modules")


if __name__ == '__main__':
    pdf = Canvas(filename="annotations.pdf", pagesize=A4)
    annotations(pdf)
    pdf.showPage()
    pdf.save()
