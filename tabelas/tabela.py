from reportlab.platypus import SimpleDocTemplate, TableStyle, Table
from reportlab.lib.colors import red, blue, green, black
from reportlab.lib.units import inch


pdf = SimpleDocTemplate(filename="tabela.pdf")
flow = list()

data = [
    ['00', '01', '02', '03', '04'],
    ['10', '11', '12', '13', '14'],
    ['20', '21', '22', '23', '24'],
    ['30', '31', '32', '33', '34']
]

t = Table(data=data, colWidths=5*[0.4*inch], rowHeights=4*[0.4*inch])
t.setStyle(TableStyle([
    ('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
    ('TEXTCOLOR', (1, 1), (-2, -2), red),

    ('VALIGN', (0, 0), (0, -1), 'TOP'),
    ('TEXTCOLOR', (0, 0), (0, -1), blue),

    ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
    ('TEXTCOLOR', (0, -1), (-1, -1), green),

    ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),

    ('INNERGRID', (0, 0), (-1, -1), 0.25, black),
    ('BOX', (0, 0), (-1, -1), 0.25, black),
])
)

flow.append(t)
pdf.build(flowables=flow)
