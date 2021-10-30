from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Preformatted, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from relatorio.models import Contact


# ------Classe usada pela View detail_pdf2 -------
class DetailPdf:  # Funcionando OK!
    def __init__(self, buffer, request, pk, pagesize):
        self.buffer = buffer
        self.request = request
        self.pk = pk
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    def detail_pdf2(self):
        buffer = self.buffer
        pk = self.pk
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                title='Relatório',
                                author='JC9',
                                subject='Detail Client',
                                pagesize=self.pagesize)
        flow_obj = list()

        # ----Detail object--------
        contact = Contact.objects.get(id=pk)

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

        flow_obj.append(Paragraph(text='Nome: ' + contact.first_name, style=styles['Normal']))
        flow_obj.append(Paragraph(text='Sobrenome: ' + contact.last_name, style=styles['Normal']))
        flow_obj.append(Preformatted(text='Idade: ' + str(contact.age), style=styles['Normal']))
        flow_obj.append(Spacer(width=0.5*inch, height=0.5*inch))

        # Configuração na Primeira página
        def myonfirstpage(canvas, document):
            canvas.saveState()

            # Configuração do Título da Primeira Página
            canvas.setFont(psfontname="Helvetica-Bold", size=18)
            canvas.drawCentredString(x=3 * inch, y=11 * inch, text="Título DetailPdf 2")

            # Configuração do rodapé da Primeira Página
            canvas.setFont(psfontname="Times-Roman", size=12)
            canvas.drawString(x=3 * inch, y=0.75 * inch, text="Página 1")

            canvas.restoreState()

        # Configuração das demais páginas
        def mylaterpages(canvas, document):
            canvas.saveState()

            canvas.setFont(psfontname="Times-Roman", size=9)
            canvas.drawString(x=1 * inch, y=0.75 * inch, text="Página")
            canvas.drawString(x=1.5 * inch, y=0.75 * inch, text=str(canvas.getPageNumber()))
            canvas.restoreState()

        # Construção do objeto flutuante
        doc.build(flowables=flow_obj, onFirstPage=myonfirstpage, onLaterPages=mylaterpages)

        # Define a variável para o buffer e pega todos valores
        pdf = buffer.getvalue()

        # Fecha o buffer
        buffer.close()

        # Retorna a request
        return pdf
