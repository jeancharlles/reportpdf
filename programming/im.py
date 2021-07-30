from reportlab.platypus import Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

pdf = SimpleDocTemplate(filename="im.pdf")
style = getSampleStyleSheet()
style_normal = style['Normal']
flow = list()

im = Image(filename="img.png", width=2*inch, height=1.5*inch)
# im = Image(filename="img.png")
im.hAlign = 'CENTER'
# im.hAlign = 'LEFT'
# im.hAlign = 'RIGHT'

flow.append(im)

pdf.build(flowables=flow)
