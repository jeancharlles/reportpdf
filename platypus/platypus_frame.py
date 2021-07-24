from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame

styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']

story = list()

# add some flowables
story.append(Paragraph("This is a Heading", styleH))

story.append(Paragraph("This is a paragraph in <i>Normal</i> style.", styleN))

c = Canvas(filename='platypus_frame.pdf')

f = Frame(x1=1*inch, y1=1*inch, width=6*inch, height=9*inch, showBoundary=1)
f.addFromList(drawlist=story, canv=c)
c.save()
