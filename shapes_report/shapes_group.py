from reportlab.graphics.shapes import Line, Drawing, Group, String
from reportlab.graphics import renderPDF
from reportlab.lib.colors import black

d = Drawing(width=400, height=200)

Axis = Group(
    Line(x1=0, y1=0, x2=100, y2=0),  # x axis
    Line(x1=0, y1=0, x2=0, y2=50),  # y axis
    Line(x1=0, y1=10, x2=10, y2=10),  # ticks on y axis
    Line(x1=0, y1=20, x2=10, y2=20),
    Line(x1=0, y1=30, x2=10, y2=30),
    Line(x1=0, y1=40, x2=10, y2=40),
    Line(x1=10, y1=0, x2=10, y2=10),  # ticks on x axis
    Line(x1=20, y1=0, x2=20, y2=10),
    Line(x1=30, y1=0, x2=30, y2=10),
    Line(x1=40, y1=0, x2=40, y2=10),
    Line(x1=50, y1=0, x2=50, y2=10),
    Line(x1=60, y1=0, x2=60, y2=10),
    Line(x1=70, y1=0, x2=70, y2=10),
    Line(x1=80, y1=0, x2=80, y2=10),
    Line(x1=90, y1=0, x2=90, y2=10),
    String(x=20, y=35, text='Axes', fill=black)
)

# first group
firstAxisGroup = Group(Axis)
firstAxisGroup.translate(dx=10, dy=10)
d.add(node=firstAxisGroup, name='firstAxisGroup')

# second group
secondAxisGroup = Group(Axis)
secondAxisGroup.translate(dx=150, dy=10)
secondAxisGroup.rotate(theta=15)
d.add(node=secondAxisGroup, name='secondAxisGroup')

# third group
thirdAxisGroup = Group(Axis)
thirdAxisGroup.translate(dx=300, dy=10),
thirdAxisGroup.rotate(theta=30)
d.add(node=thirdAxisGroup, name='thirdAxisGroup')

renderPDF.drawToFile(d=d, fn="shapes_group.pdf", msg="Group")
