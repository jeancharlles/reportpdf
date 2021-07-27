from reportlab.lib.colors import green, red, blue, lavender, orange, pink, khaki, beige, black, limegreen
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

pdf = SimpleDocTemplate(filename="tabela_image.pdf", pagesize=A4)

flow = list()

stylesheet = getSampleStyleSheet()

img = Image(filename='reportlab.bmp')
img.drawHeight = 1.25*inch*img.drawHeight/img.drawWidth
img.drawWidth = 1.25*inch

p0 = Paragraph(
    """
    A Paragraph
    """,
    stylesheet["BodyText"])

p1 = Paragraph(
    """ 
    The ReportLab Left
    Logo
    Image
    """,
    stylesheet['BodyText'])

data = [
    ['A', 'B', 'C', p0, 'D'],
    ['00', '01', '02', [img, p1], '04'],
    ['10', '11', '12', [p1, img], '14'],
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
        ('BACKGROUND', (0, 0), (0, 1), pink),
        ('BACKGROUND', (1, 1), (1, 2), lavender),
        ('BACKGROUND', (2, 2), (2, 3), orange),
        ('BOX', (0, 0), (-1, -1), 2, black),
        ('GRID', (0, 0), (-1, -1), 0.5, black),
        ('VALIGN', (3, 0), (3, 0), 'BOTTOM'),
        ('BACKGROUND', (3, 0), (3, 0), limegreen),
        ('BACKGROUND', (3, 1), (3, 1), khaki),
        ('ALIGN', (3, 1), (3, 1), 'CENTER'),
        ('BACKGROUND', (3, 2), (3, 2), beige),
        ('ALIGN', (3, 2), (3, 2), 'LEFT')
    ]
)

t._argW[3] = 1.5*inch
flow.append(t)

pdf.build(flowables=flow)
