from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate(filename="list_flowable.pdf")
style = getSampleStyleSheet()
style_normal = style["Normal"]
story = list()
t = ListFlowable(flowables=[
        Paragraph(text="Item no.1", style=style_normal),
        ListItem(Paragraph(text="Item no. 2", style=style_normal), bulletColor="green", value=7),
        ListFlowable([
            Paragraph(text="sublist item 1", style=style_normal),
            ListItem(Paragraph('sublist item 2', style_normal), bulletColor='red', value='square')
            ],
            bulletType='bullet',
            start='square',
        ),
        Paragraph("Item no.4", style_normal),
    ],
    bulletType='i'
    )

story.append(t)

pdf.build(flowables=story)
