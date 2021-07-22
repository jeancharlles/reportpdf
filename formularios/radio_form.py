from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm
from reportlab.lib.colors import green, blue


def translate(canvas):
    canvas.translate(2*cm, 7*cm)


def scale(canvas):
    canvas.scale(1.2, 1.2)


def radio(canvas):
    canvas.drawString(x=50, y=110, text='Selecione uma Opção:')

    canvas.drawString(x=50, y=105, text='Sim:')
    canvas.acroForm.radio(
        name='radio1',
        value='Sim',
        tooltip='Sim',
        selected=True,
        shape='circle',
        x=65,
        y=105,
        buttonStyle='circle',
        borderStyle='bevelled',
        borderWidth=2,
        borderColor=blue,
        fillColor=green,
        textColor=blue,
        forceBorder=True
    )

    canvas.drawString(x=100, y=105, text='Não:')
    canvas.acroForm.radio(
        name='radio1',
        value='Não',
        tooltip='Não',
        selected=False,
        shape='circle',
        x=90,
        y=105,
        buttonStyle='circle',
        borderStyle='bevelled',
        borderWidth=2,
        borderColor=blue,
        fillColor=green,
        textColor=blue,
        forceBorder=True
    )


if __name__ == '__main__':
    pdf = Canvas(filename='radio_form.pdf')
    translate(pdf)
    scale(pdf)
    radio(pdf)
    pdf.showPage()
    pdf.save()
