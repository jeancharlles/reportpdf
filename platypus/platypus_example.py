from reportlab.platypus import Paragraph, SimpleDocTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import red
from reportlab.pdfgen import canvas


pdf = SimpleDocTemplate(filename="platypus_example.pdf")
flow_obj = []
styles = getSampleStyleSheet()
text = """
hello from total technology
"""
para_text = Paragraph(text=text, style=styles["Normal"])

for i in range(1, 10):
    flow_obj.append(para_text)
    flow_obj.append(PageBreak())


def gonumpage(flowdoc, p):
    s = flowdoc.getPageNumber()
    s = str(s)
    flowdoc.setFillColor(aColor=red)
    flowdoc.drawCentredString(300, 10, s)
    flowdoc.saveState()


pdf.build(flowables=flow_obj, onFirstPage=gonumpage, onLaterPages=gonumpage, canvasmaker=canvas.Canvas)
