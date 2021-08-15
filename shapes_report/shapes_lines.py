from reportlab.graphics.shapes import Drawing, Line, PolyLine
from reportlab.lib.colors import red, purple, blue
from reportlab.graphics import renderPDF

d = Drawing(width=400, height=200)

# Linha Azul
line1 = Line(x1=50, y1=50, x2=300, y2=100)
line1.strokeColor = blue
line1.strokeWidth = 5

# Linha Vermelha Pontilhada
line2 = Line(x1=50, y1=100, x2=300, y2=50)
line2.strokeColor = red
line2.strokeWidth = 10
line2.strokeDashArray = [10, 20]

# Linha Zig-Zag
poli = PolyLine(points=[120, 110,
                        130, 150,
                        140, 110,
                        150, 150,
                        160, 110,
                        170, 150,
                        180, 110,
                        190, 150,
                        200, 110]
                )
poli.strokeWidth = 2
poli.strokeColor = purple

# Adicionar todas as linhas
d.add(node=line1, name='line1')
d.add(node=line2, name='line2')
d.add(node=poli, name='poli')

# Renderizar PDF
renderPDF.drawToFile(d=d, fn="shapes_lines.pdf", msg="Lines")
