from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import yellow, red, black, white
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from desenhos.penciltip import pencitltip


def translate(canvas):
    canvas.translate(dx=5*cm, dy=12*cm)


def scale(canvas):
    canvas.scale(x=1.0, y=1.0)


def pencil(canvas, text):
    u = 1*inch/10.0
    canvas.setStrokeColor(black)  # Cor do traço ou borda
    canvas.setLineWidth(4)  # Largura da linha do traço

    # Borracha Vermelha
    canvas.setFillColor(red)
    canvas.circle(x_cen=30*u, y_cen=5*u, r=5*u, stroke=1, fill=1)

    # Retângulo Amarelo
    canvas.setFillColor(yellow)
    canvas.rect(x=10*u, y=0, width=20*u, height=10*u, stroke=1, fill=1)

    # Retângulo Preto
    canvas.setFillColor(black)
    canvas.rect(x=23*u, y=0, width=8*u, height=10*u, stroke=0, fill=1)

    # Retângulo com arredondamento
    canvas.roundRect(x=14*u, y=3.5*u, width=8*u, height=3*u, radius=1.5*u, stroke=1, fill=1)

    # Duas Faixa Brancas
    canvas.setFillColor(white)
    canvas.rect(x=25*u, y=1*u, width=1.2*u, height=8*u, stroke=0, fill=1)
    canvas.rect(x=27.5*u, y=1*u, width=1.2*u, height=8*u, stroke=0, fill=1)

    # Texto Nº 2
    canvas.setFont(psfontname="Times-Roman", size=3*u)
    canvas.drawCentredString(x=18*u, y=4*u, text=text)

    pencitltip(canvas, debug=0)


if __name__ == "__main__":
    pdf = Canvas(filename="pencil.pdf", pagesize=A4)
    texto = "Nº 2"
    translate(pdf)
    scale(pdf)
    pencil(pdf, text=texto)
    pdf.showPage()
    pdf.save()
