from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus.flowables import DocAssign, DocExec, DocPara, DocIf, DocWhile

doc = SimpleDocTemplate(filename='programming.pdf')

normal = ParagraphStyle(name='Normal', fontName='Helvetica', fontSize=8.5, leading=11)
header = ParagraphStyle(name='Heading1', parent=normal, fontSize=14, leading=19, spaceAfter=6, keepWithNext=1)

story = [
    # DocAssign(var='currentFrame', expr='doc.frame.id'),
    # DocAssign(var='currentPageTemplate', expr='doc.pageTemplate.id'),
    # DocAssign(var='aW', expr='availableWidth'),
    # DocAssign(var='aH', expr='availableHeight'),
    # DocAssign(var='aWH', expr='availableWidth,availableHeight'),

    DocAssign(var='i', expr=3),

    DocIf(cond='i>3',
          thenBlock=Paragraph('The value of i is larger than 3', normal),
          elseBlock=Paragraph('The value of i is not larger than 3', normal)),

    DocIf(cond='i==3',
          thenBlock=Paragraph('The value of i is equal to 3', normal),
          elseBlock=Paragraph('The value of i is not equal to 3', normal)),

    DocIf(cond='i<3',
          thenBlock=Paragraph('The value of i is less than 3', normal),
          elseBlock=Paragraph('The value of i is not less than 3', normal)),

    DocWhile(cond='i',
             whileBlock=[DocPara('i', format='The value of i is %(__expr__)d', style=normal),
                         DocExec('i-=1')]),

    # DocPara(expr='repr(doc._nameSpace)', escape=True),
]

doc.build(story)
