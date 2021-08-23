from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4

styleSheet = getSampleStyleSheet()
style = styleSheet['BodyText']
flow_obj = Paragraph(text='This is a very silly example', style=style)
canv = Canvas(filename='platypus_flowables.pdf', pagesize=A4)

aW = 460  # available width and height
aH = 800

w, h = flow_obj.wrap(availWidth=aW, availHeight=aH)  # find required space

if w <= aW and h <= aH:
    flow_obj.drawOn(canvas=canv, x=0, y=aH)
    aH = aH - h  # reduce the available height
    canv.save()
else:
    raise ValueError
