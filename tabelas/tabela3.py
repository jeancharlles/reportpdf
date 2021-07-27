from reportlab.pdfgen import canvas
from reportlab.lib.colors import green, red, blue, pink
from reportlab.platypus import SimpleDocTemplate, Table


pdf = SimpleDocTemplate(filename="tabela3.pdf")

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
        ('GRID', (1, 1), (-2, -2), 1, green),
        ('BOX', (0, 0), (1, -1), 2, red),
        ('LINEABOVE', (1, 2), (-2, 2), 1, blue),
        ('LINEBEFORE', (2, 1), (2, -2), 1, pink),
        ]
)

flow.append(t)

pdf.build(flowables=flow, canvasmaker=canvas.Canvas)  # Aparentemente essa informação pode ser suprimida
