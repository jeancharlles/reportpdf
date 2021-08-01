from reportlab.platypus import Paragraph, SimpleDocTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.tableofcontents import SimpleIndex

pdf = SimpleDocTemplate(filename="simple_index_dot.pdf")
styles = getSampleStyleSheet()
story = list()

text = """
The first <index item="terma, termb, termc" />term of this paragraph is indexed.<br/>
The second <index item="terma, termd" /> term is indexed
"""
p = Paragraph(text=text, style=styles['Normal'])
story.append(p)
story.append(PageBreak())

text1 = """
The third <index item="word" />word of this paragraph is indexed.
"""
p1 = Paragraph(text=text1, style=styles['Normal'])
story.append(p1)
story.append(PageBreak())

text2 = """
<index item="comma,,, delta" />Comma
"""
# <index item="comma(,,), ,, ,... " />Comma
p2 = Paragraph(text=text2, style=styles['Normal'])
story.append(p2)
story.append(PageBreak())


index = SimpleIndex(dot='.')
story.append(index)

pdf.build(flowables=story, canvasmaker=index.getCanvasMaker())
