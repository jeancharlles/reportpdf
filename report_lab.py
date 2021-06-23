from reportlab.pdfgen import canvas


def hello(c):
    c.drawString(100, 100, "Hello World")
    c = canvas.Canvas("hello.pdf")
    c.showPage()
    c.save()

