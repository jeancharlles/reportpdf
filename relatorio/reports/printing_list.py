from django.contrib.auth.models import User
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Preformatted, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from relatorio.models import Contact


# ------Classe que usa o Model com Paginas e retorna a request para a View-----#
class ListPdf:  # Funcionando OK!
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    def lista(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                title='Printing',
                                author='JC9',
                                subject='Lista de Clientes',
                                pagesize=self.pagesize)
        flow_obj = list()

        # Configura a variável do Model--
        contacts = Contact.objects.all()

        # Define o estilo e configurações de parágrafo
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

        users = User.objects.all()

        flow_obj.append(Paragraph('Usuário', styles['Heading1']))

        for i, user in enumerate(users):
            flow_obj.append(Paragraph(text=user.get_full_name(), style=styles['Normal']))
            flow_obj.append(Spacer(width=0.5 * inch, height=0.5 * inch))

        # Configuração do objeto flutuante e da visualização
        for i, contact in enumerate(contacts):
            flow_obj.append(Paragraph(text='Nome:' + contact.first_name, style=styles['h1']))
            flow_obj.append(Paragraph(text='Sobrenome: ' + contact.last_name, style=styles['h2']))
            flow_obj.append(Preformatted(text='Idade:' + str(contact.age), style=styles['h3']))
            flow_obj.append(Spacer(width=0.5*inch, height=0.5*inch))

        # Configuração na Primeira página
        def myonfirstpage(canvas, document):
            canvas.saveState()

            # Configuração do Título
            x = 3.5
            canvas.setFont(psfontname="Helvetica-Bold", size=18)
            canvas.drawCentredString(x=4 * inch, y=11 * inch, text="Título")

            # Configuração do rodapé da primeira página
            canvas.setFont(psfontname="Helvetica", size=12)
            canvas.drawString(x=x * inch, y=0.75 * inch, text="Introdução")

            canvas.restoreState()

        # Configuração das demais páginas
        def mylaterpages(canvas, document):
            canvas.saveState()

            # Configuração do rodapé das páginas seguintes
            x = 3.5*inch
            canvas.setFont(psfontname="Helvetica", size=12)
            canvas.drawString(x=x, y=0.75 * inch, text="Página")
            canvas.drawString(x=4.1*inch, y=0.75 * inch, text=str(canvas.getPageNumber()))

            canvas.restoreState()

        # Construção do objeto flutuante
        doc.build(flowables=flow_obj, onFirstPage=myonfirstpage, onLaterPages=mylaterpages)
        # doc.build(lines)

        # Define a variável para o buffer e pega todos valores
        pdf = buffer.getvalue()

        # Fecha o buffer
        buffer.close()

        # Retorna a request
        return pdf
