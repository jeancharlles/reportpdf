from reportlab.lib.colors import black, green, red, pink, lavender, orange, grey, blue
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import A4

pdf = SimpleDocTemplate(filename="tabela4.pdf", pagesize=A4)

flow = list()

data = [
    ['00', '01', '02', '03', '04'],
    ['10', '11', '12', '13', '14'],
    ['20', '21', '22', '23', '24'],
    ['30', '31', '32', '33', '34']
]

t = Table(
    data=data,
    style=[
        ('GRID', (0, 0), (-1, -1), 0.5, grey),
        ('GRID', (1, 1), (-2, -2), 1, green),
        ('BOX', (0, 0), (1, -1), 2, red),
        ('BOX', (0, 0), (-1, -1), 2, black),
        ('LINEABOVE', (1, 2), (-2, 2), 1, blue),
        ('LINEBEFORE', (2, 1), (2, -2), 1, pink),
        ('BACKGROUND', (0, 0), (0, 1), pink),
        ('BACKGROUND', (1, 1), (1, 2), lavender),
        ('BACKGROUND', (2, 2), (2, 3), orange),
    ])

flow.append(t)

pdf.build(flowables=flow)
