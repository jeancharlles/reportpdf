from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate(filename="list_flowable2.pdf")
style = getSampleStyleSheet()
style_normal = style["Normal"]
story = list()

t = ListFlowable(flowables=[
        Paragraph(text="Item no.1", style=style_normal),
        ListItem(Paragraph(text="Item no. 2", style=style_normal), bulletColor="green", value=7),
        ListFlowable([
            Paragraph(text="sublist item 1", style=style_normal),
            ListItem(Paragraph(text='sublist item 2', style=style_normal), bulletColor='red', value='square'),
            Paragraph(text="sublist item 3", style=style_normal)
            ],
            bulletType='bullet',
            start='circle',
            bulletColor='blue',
        ),
        Paragraph(text="Item no.4", style=style_normal),
    ],
    bulletType='1'
    )

story.append(t)

pdf.build(flowables=story)
