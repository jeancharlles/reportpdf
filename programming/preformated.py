from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Preformatted

pdf = SimpleDocTemplate(filename="preformated.pdf")
flow = list()

stylesheet = getSampleStyleSheet()
normalStyle = stylesheet['Code']

text = '''
class XPreformatted(Paragraph):
def __init__(self, text, style, bulletText = None, frags=None, caseSensitive=1):
    self.caseSensitive = caseSensitive
    if maximumLineLength and text:
        text = self.stopLine(text, maximumLineLength, splitCharacters)
        cleaner = lambda text, dedent=dedent: ''.join(_dedenter(text or '',dedent))
    self._setup(text, style, bulletText, frags, cleaner)
'''

t = Preformatted(text=text, style=normalStyle, maxLineLength=60, newLineChars='> ')

flow.append(t)
pdf.build(flowables=flow)
