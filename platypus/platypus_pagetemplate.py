from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate


styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading2']

story = list()

story.append(Paragraph(text="This a Heading", style=styleH))
story.append(Paragraph(text="This is a paragraph in normal <i> Itálico </i> style", style=styleN))

doc = SimpleDocTemplate(filename='platypus_pagetemplate.pdf', pagesize=letter)
doc.build(flowables=story)
