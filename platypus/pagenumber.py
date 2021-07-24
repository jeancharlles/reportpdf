from reportlab.pdfgen import canvas

pdf = canvas.Canvas(filename="pagenumber.pdf")

pdf.drawCentredString(300, 10, str(pdf.getPageNumber()))
pdf.showPage()

pdf.drawCentredString(300, 10, str(pdf.getPageNumber()))
pdf.showPage()

pdf.drawCentredString(300, 10, str(pdf.getPageNumber()))
pdf.showPage()

pdf.save()
