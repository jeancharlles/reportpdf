from reportlab.lib.colors import grey, palegreen, pink
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import A4

pdf = SimpleDocTemplate(filename="tabela5.pdf", pagesize=A4)

flow = list()

data = [
    ['Top\nLeft', '', '02', '03', '04'],
    ['', '', '12', '13', '14'],
    ['20', '21', '22', 'Bottom\nRight', ''],
    ['30', '31', '32', '', '']
]

t = Table(
    data=data,
    style=[
        ('GRID', (0, 0), (-1, -1), 0.5, grey),
        ('BACKGROUND', (0, 0), (1, 1), palegreen),
        ('SPAN', (0, 0), (1, 1)),
        ('BACKGROUND', (-2, -2), (-1, -1), pink),
        ('SPAN', (-2, -2), (-1, -1)),
    ]
)

flow.append(t)

pdf.build(flowables=flow)
