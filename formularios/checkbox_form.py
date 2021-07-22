from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red, green, blue, gold


def checkbox(canvas):
    canvas.acroForm.checkbox(
        name='CB0',
        tooltip='Field CB0',
        checked=True,
        x=72, y=72+4*36,
        buttonStyle='diamond',
        borderStyle='bevelled',
        borderWidth=2,
        borderColor=blue,
        fillColor=gold,
        textColor=blue,
        forceBorder=True)


if __name__ == '__main__':
    pdf = Canvas("checkbox_form.pdf")
    checkbox(pdf)
    pdf.showPage()
    pdf.save()
