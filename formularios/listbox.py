from reportlab.pdfgen import canvas
from reportlab.lib.colors import magenta, pink, blue


def create_simple_listboxes():
    c = canvas.Canvas('listbox.pdf')

    c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Listboxes')
    c.setFont("Courier", 14)
    form = c.acroForm

    c.drawString(10, 650, 'Choose a letter:')
    options = [('A', 'Av'), 'B', ('C', 'Cv'), ('D', 'Dv'), 'E', ('F',), ('G', 'Gv')]
    form.listbox(name='listbox1', tooltip='Field choice1', value='A',
                 x=165, y=590,
                 width=70, height=80,
                 borderColor=magenta, fillColor=pink, textColor=blue,
                 forceBorder=True,
                 options=options,
                 fieldFlags='multiSelect')

    c.drawString(10, 500, 'Choose an animal:')
    options = [('Cat', 'cat'), ('Dog', 'dog'), ('Pig', 'pig')]
    form.listbox(name='choice2', tooltip='Field choice2', value='Cat',
                 options=options,
                 x=165, y=440,
                 width=70, height=60,
                 borderStyle='solid', borderWidth=1,
                 forceBorder=True)

    c.save()


if __name__ == '__main__':
    create_simple_listboxes()
