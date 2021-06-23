from reportlab.pdfgen import canvas


def hello(ca):
    ca.drawString(10, 10, "Olá Mundo")


if __name__ == '__main__':

    c = canvas.Canvas("hello.pdf")
    hello(c)
    c.showPage()
    c.save()
