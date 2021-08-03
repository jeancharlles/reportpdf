from reportlab.platypus import Paragraph, SimpleDocTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.tableofcontents import SimpleIndex


pdf = SimpleDocTemplate(filename="simple_index.pdf")
flow_obj = list()
styles = getSampleStyleSheet()

text = """
this is sample <index item="index"/> without index
"""
p_text = Paragraph(text=text, style=styles['Normal'])

text1 = """
this is sample <index item="reportlab"/> with reportlab index
"""
p_text1 = Paragraph(text=text1, style=styles['Normal'])

text2 = """
this is sample <index item="flowable"/> with flowable index
"""
p_text2 = Paragraph(text=text2, style=styles['Normal'])

index = SimpleIndex()

for i in range(1, 4):
    flow_obj.append(p_text)
    flow_obj.append(PageBreak())

for i in range(1, 4):
    flow_obj.append(p_text1)
    flow_obj.append(PageBreak())

for i in range(1, 4):
    flow_obj.append(p_text2)
    flow_obj.append(PageBreak())

flow_obj.append(index)

pdf.build(flowables=flow_obj, canvasmaker=index.getCanvasMaker())
