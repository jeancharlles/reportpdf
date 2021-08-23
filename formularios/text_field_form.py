from reportlab.pdfgen import canvas
from reportlab.lib.colors import magenta, pink, blue, green


def create_simple_form():
    c = canvas.Canvas('text_field_form.pdf')

    c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Employment Form')

    c.setFont("Courier", 14)
    form = c.acroForm

    c.drawString(10, 650, 'First Name:')
    form.textfield(name='fname', tooltip='First Name',
                   x=110, y=635,
                   width=300,
                   borderStyle='inset', borderColor=magenta, fillColor=pink,
                   textColor=blue, forceBorder=True)

    c.drawString(10, 600, 'Last Name:')
    form.textfield(name='lname', tooltip='Last Name',
                   x=110, y=585,
                   width=300,
                   borderStyle='inset',
                   borderColor=green, fillColor=magenta, textColor=blue,
                   forceBorder=True)

    c.drawString(x=10, y=550, text='Address:')
    form.textfield(name='address', tooltip='Address',
                   x=110, y=535,
                   width=400,
                   borderStyle='inset',
                   forceBorder=True)

    c.drawString(10, 500, 'City:')
    form.textfield(name='city', tooltip='City',
                   x=110, y=485,
                   borderStyle='inset',
                   forceBorder=True)

    c.drawString(250, 500, 'State:')
    form.textfield(name='state', tooltip='State',
                   x=350, y=485,
                   borderStyle='inset',
                   forceBorder=True)

    c.drawString(10, 450, 'Zip Code:')
    form.textfield(name='zip_code', tooltip='Zip Code',
                   x=110, y=435,
                   borderStyle='inset',
                   forceBorder=True)

    c.save()


if __name__ == '__main__':
    create_simple_form()
