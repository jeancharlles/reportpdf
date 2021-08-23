# from reportlab.pdfgen import canvas
# from django.contrib.auth.models import User
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from .models import Contact


class MyPrint:
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        # elif pagesize == 'Letter':
        #     self.pagesize = letter
        self.width, self.height = self.pagesize

    def print_users(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                title='Printing',
                                author='JC9',

                                pagesize=self.pagesize)
        elements = list()
        lines = list()
        contacts = Contact.objects.all()

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

        # users = User.objects.all()
        # elements.append(Paragraph('My User Names', styles['Heading1']))
        # for i, user in enumerate(users):
        #     elements.append(Paragraph(user.get_full_name(), styles['Normal']))

        # Lista todos os objetos e adiciono cada a lista lines

        for contact in contacts:
            lines.append(f'Nome1: {contact.first_name}')
            lines.append(f'Sobrenome1: ' + contact.last_name)

        for i, contact in enumerate(contacts):
            elements.append(Paragraph(text='Nome2:' + contact.first_name, style=styles['Heading1']))
            elements.append(Paragraph(text='Sobrenome2: ' + contact.last_name, style=styles['Heading1']))
            elements.append(Preformatted(text='Idade2:' + str(contact.age), style=styles['Heading1'], newLineChars=" "))
            # elements.append(Paragraph(text=" "))

        def myonfirstpage(canvas, document):
            canvas.saveState()
            canvas.setFont(psfontname="Helvetica-Bold", size=18)
            canvas.drawCentredString(x=3 * inch, y=11 * inch, text="Title")
            canvas.setFont(psfontname="Times-Roman", size=12)
            canvas.drawString(x=3 * inch, y=0.75 * inch, text="Introdução")
            canvas.restoreState()

        def mylaterpages(canvas, document):
            canvas.saveState()
            canvas.setFont(psfontname="Times-Roman", size=9)
            canvas.drawString(x=1 * inch, y=0.75 * inch, text="Página")
            canvas.drawString(x=1.5 * inch, y=0.75 * inch, text=str(canvas.getPageNumber()))
            canvas.restoreState()

        doc.build(flowables=elements, onFirstPage=myonfirstpage, onLaterPages=mylaterpages)
        # doc.build(lines)

        pdf = buffer.getvalue()
        buffer.close()

        return pdf
