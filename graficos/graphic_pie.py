from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.colors import red
from reportlab.graphics import renderPDF

# Criação do formato (Altura e Largura)
d = Drawing(width=400, height=200)

# Cria a instance pc
pc = Pie()

pc.x = 150
pc.y = 50

pc.data = [10, 20, 30, 40, 50, 60]
pc.labels = ['a', 'b', 'c', 'd', 'e', 'f']

pc.slices.strokeWidth = 0.1

# slices[3] equivale ao label "d"
pc.slices[3].popout = 10  # distância da fatia ao raio
pc.slices[3].strokeWidth = 1  # Largura da linha da fatia d
pc.slices[3].strokeDashArray = [2, 2]  # Desenha o tracejado
pc.slices[3].labelRadius = 1.25  # distância do label d em relação ao raio
pc.slices[3].fontColor = red  # cor da fonte do label d
d.add(pc, '')

renderPDF.drawToFile(d=d, fn="graphic_pie.pdf", msg="My Graphic Pie")
