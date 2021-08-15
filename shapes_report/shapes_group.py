from reportlab.graphics.shapes import Line, Drawing, Group, String
from reportlab.graphics import renderPDF
from reportlab.lib.colors import black

d = Drawing(width=400, height=200)

Axis = Group(
    Line(x1=0, y1=0, x2=100, y2=0),  # x axis # y axis
    Line(0, 0, 0, 50),  # y axis
    Line(0, 10, 10, 10),  # ticks on y axis
    Line(0, 20, 10, 20),
    Line(0, 30, 10, 30),
    Line(0, 40, 10, 40),
    Line(10, 0, 10, 10),  # ticks on x axis
    Line(20, 0, 20, 10),
    Line(30, 0, 30, 10),
    Line(40, 0, 40, 10),
    Line(50, 0, 50, 10),
    Line(60, 0, 60, 10),
    Line(70, 0, 70, 10),
    Line(80, 0, 80, 10),
    Line(90, 0, 90, 10),
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
