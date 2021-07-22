from reportlab.pdfgen import canvas


def hello(c):
    c.drawString(100, 300, "Hello World")


if __name__ == '__main__':
    pdf = canvas.Canvas(filename="form_password.pdf")
    hello(pdf)
    pdf.showPage()
    pdf.save()
