from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.colors import red, green


pdf = SimpleDocTemplate(filename="tabela2.pdf")
flow = list()

data = [
    ['00', '01', '02', '03', '04'],
    ['10', '11', '12', '13', '14'],
    ['20', '21', '22', '23', '24'],
    ['30', '31', '32', '33', '34']
]

t = Table(data)
t.setStyle(TableStyle([
    ('BACKGROUND', (1, 1), (-2, -2), green),
    ('TEXTCOLOR', (0, 0), (1, -1), red)])
)

flow.append(t)
pdf.build(flowables=flow)
