from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, XPreformatted

pdf = SimpleDocTemplate(filename="xpreformated.pdf")
flow = list()

stylesheet = getSampleStyleSheet()
normalStyle = stylesheet['Code']

text = '''
This is a non rearranging form of the <b>Paragraph</b> class;
<b><font color=red>XML</font></b> tags are allowed in <i>text</i> and have the same meanings as for the <b>Paragraph</b>
 class.
As for <b>Preformatted</b>, 
if dedent is non zero <font color="red" size="+1">dedent</font>
    common leading spaces will be removed from the
front of each line.
You can have &amp; amp; style entities as well for &amp; &lt; &gt; and &quot;.
'''

t = XPreformatted(text=text, style=normalStyle, dedent=0)

flow.append(t)
pdf.build(flowables=flow)
