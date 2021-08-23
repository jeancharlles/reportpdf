from reportlab.pdfgen import canvas
from reportlab.lib import pdfencrypt

enc = pdfencrypt.StandardEncryption(userPassword="rptlab", canPrint=0)


def hello(c):
    c.drawString(100, 300, "Hello World")


if __name__ == '__main__':
    pdf = canvas.Canvas(filename="form_password.pdf", encrypt=enc)
    hello(pdf)
    pdf.showPage()
    pdf.save()
