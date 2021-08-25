from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.platypus import Paragraph, Frame, Image
from reportlab.lib.colors import red


c = Canvas(filename='platypus_frame.pdf')

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']

story = list()
drawlist = list()

# add some flowables
story.append(Paragraph("This is a Heading", styleH))
story.append(Paragraph("This is a paragraph in <i>Normal</i> style.", styleN))

drawlist.append(Image(filename="logo.png", hAlign='LEFT'))
# drawlist.append(Image(filename="logo.png", hAlign='RIGHT'))
# drawlist.append(Image(filename="logo.png", hAlign='CENTER'))

c.setStrokeColor(aColor='red')
f = Frame(x1=1*inch, y1=5*inch, width=6*inch, height=2*inch, showBoundary=1)
f.addFromList(drawlist=story, canv=c)

c.setStrokeColor(aColor='blue')
f = Frame(x1=1*inch, y1=9*inch, width=4*inch, height=2*inch, showBoundary=1)
f.addFromList(drawlist=drawlist, canv=c)

c.setStrokeColor(aColor='pink')
f = Frame(x1=5.1*inch, y1=9*inch, width=2*inch, height=2*inch, showBoundary=1)
drawlist.append(Paragraph("POR ENTRE SI CELEBRAM AS PARTES", style=styleN))
f.addFromList(drawlist=drawlist, canv=c)

c.save()
