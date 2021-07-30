from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tableofcontents import TableOfContents

pdf = SimpleDocTemplate(filename="table_of_contents.pdf")
story = list()
toc = TableOfContents()
ps = ParagraphStyle

toc.levelStyles = [
    ps(fontName='Times-Bold', fontSize=14, name='TOCHeading1', leftIndent=20, firstLineIndent=-20, spaceBefore=5, leading=16),
    ps(fontSize=12, name='TOCHeading2', leftIndent=40, firstLineIndent=-20, spaceBefore=0, leading=12),
    ps(fontSize=10, name='TOCHeading3', leftIndent=60, firstLineIndent=-20, spaceBefore=0, leading=12),
    ps(fontSize=10, name='TOCHeading4', leftIndent=100, firstLineIndent=-20, spaceBefore=0, leading=12)
]

story.append(toc)

pdf.build(flowables=story)
