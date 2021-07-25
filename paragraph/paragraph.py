from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


pdf = SimpleDocTemplate(filename="paragraph.pdf")
flow = list()
text = """ 
<para>
Lembrem-se sempre que <u><i>vocês</i></u> podem ir 
<a href="MYANCHOR" color="blue"> além </a>
<strong>das expectativas</strong> 
<font name="Times-italic" size=14>que colocam em cima de vocês, que podem alcançar os seus sonhos</font> 
e realizar tudo o que desejam se acreditarem no seu próprio potencial.
<br></br><br></br>

<font face="times" color="red">Acreditem</font> 
em tudo o que vocês ainda têm para conquistar, tudo o que está por vir e tudo o que ainda depende de vocês. 
<br></br><br></br>

<link href="MYANCHOR" color="blue" fontName="Helvetica">Acreditem que vocês podem ir além</link> 
<strike>e tudo vai se encaixar</strike> com o <font size=14>tempo</font>.
Acesse o <a href="https://www.google.com" color="blue"><u>google</u></a> 
<nobr>averylongwordthatwontbebroken</nobr> won't be broken.
A persistência é o caminho do êxito.
<br></br><br></br>

<seq id="spam"/>, <seq id="spam"/>, <seq id="spam"/>, <seq id="spam"/>. Reset<seqreset id="spam"/>. <seq id="spam"/>, <seq id="spam"/>,
<seq id="spam"/>
<br></br><br></br>

Equation (&alpha;): <greek>e</greek> <super rise=9 size=6> <greek>ip</greek></super> = -1
<br></br><br></br>

Figure <seq template="%(Chapter) s-%(FigureNo+)s"/> - Multi-level templates
</para>
"""
stylesheet = getSampleStyleSheet()
paragraph_text = Paragraph(text=text, style=stylesheet["Normal"])
flow.append(paragraph_text)
pdf.build(flowables=flow)
