from reportlab.pdfgen import canvas
from reportlab.lib.colors import magenta, pink, blue


def create_simple_choices():
    c = canvas.Canvas('choice_form.pdf')

    c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Choices')
    c.setFont("Courier", 14)
    form = c.acroForm

    c.drawString(10, 650, 'Choose a letter:')
    options = [('A', 'Av'), 'B', ('C', 'Cv'), ('D', 'Dv'), 'E', ('F',), ('G', 'Gv')]
    form.choice(name='choice1', tooltip='Field choice1', value='A',
                options=options,
                x=165, y=645,
                width=72, height=20,
                borderColor=magenta, fillColor=pink, textColor=blue,
                forceBorder=True)

    c.drawString(10, 600, 'Choose an animal:')
    options = [('Cat', 'cat'), ('Dog', 'dog'), ('Pig', 'pig')]
    form.choice(name='choice2', tooltip='Field choice2', value='Cat',
                options=options,
                x=165, y=595,
                width=72, height=20,
                borderStyle='solid', borderWidth=1,
                forceBorder=True)

    c.save()


if __name__ == '__main__':
    create_simple_choices()
