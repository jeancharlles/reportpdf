from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate(filename="list_flowable.pdf")
styles = getSampleStyleSheet()
style_normal = styles["Normal"]
story = list()

t = ListFlowable(
    [
        Paragraph("Item no.1", style_normal),
        ListItem(Paragraph("Item no. 2", style_normal), bulletColor="green", value=5),

        ListFlowable(
            [
                Paragraph("sublist item 1", style_normal),
                ListItem(Paragraph('sublist item 2', style_normal),
                         bulletColor='red', value='square')
            ],
            bulletType='bullet',
            start='square', ),
        Paragraph("Item no.4", style_normal)
    ],
    bulletType='i')

# bulletType='1')
# bulletType='A')

story.append(t)

pdf.build(flowables=story)
