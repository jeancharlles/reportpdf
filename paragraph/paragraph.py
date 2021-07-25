from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


pdf = SimpleDocTemplate("paragraph.pdf")
flow = list()
text = """ 
Lembrem-se sempre que <strong><i>vocês</i> podem ir além das expectativas</strong> 
que colocam em cima de vocês, que podem alcançar os seus sonhos 
e realizar tudo o que desejam se acreditarem no seu próprio potencial.
<br></br><br></br>
Acreditem em tudo o que vocês ainda têm para conquistar, tudo o que está 
por vir e tudo o que ainda depende de vocês. 
<br></br><br></br>
Acreditem que vocês podem ir além e tudo vai se encaixar com o tempo.
"""
stylesheet = getSampleStyleSheet()
paragraph_text = Paragraph(text=text, style=stylesheet["Normal"])
flow.append(paragraph_text)
pdf.build(flowables=flow)
