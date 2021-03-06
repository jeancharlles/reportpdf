from io import BytesIO
from django.http import FileResponse, HttpResponse
from django.views.decorators.http import require_http_methods

# ReportLab
from platypus.platypus_intro import myfirstpage, mylaterpages, go
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm, inch
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import blue, black, green, gold, red, royalblue

# WeasyPrint
# from django.core.files.storage import FileSystemStorage
# from django.template.loader import render_to_string
from weasyprint import HTML

# Views Generics
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Model
from relatorio.models import Contact

# Printing próprios
from relatorio.reports.printing_list import ListPdf
from relatorio.reports.printing_detail import DetailPdf


class IndexView(TemplateView):
    template_name = "relatorio/index.html"


class ContactListView(ListView):
    model = Contact


class ContactDetailView(DetailView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# -----View que configura dentro dela sem usar arquivo externo
def detail_pdf(request, pk):  # Certa e Funcionando OK!
    buffer = BytesIO()

    pdf = Canvas(buffer, pagesize=A4)
    pdf.setTitle(title="Detail")
    pdf.setAuthor(author="JC9")
    pdf.setSubject(subject="Cliente")

    text_object = pdf.beginText(x=0, y=0)
    text_object.setTextOrigin(x=2*cm, y=25*cm)
    text_object.setFont(psfontname="Helvetica", size=14)

    contact = Contact.objects.get(id=pk)

    lines = list()
    lines.append(f'Nome: {contact.first_name}')
    lines.append(f'Sobrenome: ' + contact.last_name)
    lines.append(f'Idade: {contact.age}')
    lines.append(" ")

    # Insiro da lista lines cada linha em text_object
    for line in lines:
        text_object.textLines(stuff=str(line))

    # Desenho o text_object
    pdf.drawCentredString(x=10.5*cm, y=27*cm, text="Cliente")
    pdf.drawText(aTextObject=text_object)
    pdf.setFont(psfontname="Helvetica", size=14)
    pdf.drawCentredString(x=10.5*cm, y=1*cm, text=f'Página {str(pdf.getPageNumber())}')
    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=False, filename='detail.pdf')


# ----View que configura fora dela na Classe DetailPdf, usando arquivo externo printing_detail.py
@require_http_methods(['GET'])
def detail_pdf2(request, pk):  # Certa e Funcionando Tudo OK!
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="detail2.pdf"'
    response['Content-Disposition'] = 'inline; filename="detail2.pdf"'
    buffer = BytesIO()
    report = DetailPdf(buffer, request=request, pk=pk, pagesize='A4')
    pdf = report.detail_pdf2()
    response.write(pdf)
    return response


# ----View que configura fora dela uma lista Models com página e da classe ListPdf em arquivo externo printing_list.py
@require_http_methods(['GET'])
def lista(request):  # Certa e Funcionando Tudo OK!
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="printing.pdf"'
    response['Content-Disposition'] = 'inline; filename="printing.pdf"'
    buffer = BytesIO()
    report = ListPdf(buffer, 'A4')  # define a variável report que instancia a classe ListPdf
    pdf = report.lista()  # aqui instancia o pdf buscando a função lista em printing_list.py
    response.write(pdf)
    return response


# Não funciona
def reportpdfpage(request):
    go()


# ----Exemplo ReportLab com Model e Numeração de Página Única---------#
def reportpdf(request):

    # ------- Configuração da Página-------------
    buffer = BytesIO()
    pdf = Canvas(buffer, pagesize=A4)
    pdf.setTitle(title="Listagem de Nomes")
    pdf.setAuthor(author="JC9")
    pdf.setSubject(subject="Listagem de Nomes dos Clientes")

    # --------Criação e Configuração do text_object-----
    text_object = pdf.beginText(x=0, y=0)
    text_object.setTextOrigin(x=2*cm, y=27*cm)
    text_object.setFont(psfontname="Helvetica", size=12)

    # --------Configuração do Model ---------------
    contacts = Contact.objects.all()

    # Cria-se a lista e adiciono todos os objetos
    lines = list()
    for contact in contacts:
        lines.append(f'Nome: {contact.first_name}')
        lines.append(f'Sobrenome: ' + contact.last_name)
        lines.append(f'Idade: {contact.age}')
        lines.append(" ")

    # Retiro da lista cada objeto em text_object
    for line in lines:
        text_object.textLines(stuff=str(line))

    # --------Desenho o text_object com numeração de páginas--------------
    pdf.drawText(aTextObject=text_object)
    pdf.setFont(psfontname="Helvetica", size=12)
    pdf.drawCentredString(x=10.5*cm, y=2*cm, text=f'Página {str(pdf.getPageNumber())}')
    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=False, filename='report.pdf')


# ----Exemplo ReportLab com Model que configura dentro dela---------------#
class PDFView(View):
    @staticmethod
    def get(request, *args, **kwargs):

        # ------- Configuração da Página-------------
        buffer = BytesIO()
        pdf = Canvas(buffer, pagesize=A4)
        pdf.setTitle(title="Lista de Nomes")

        # -----------------1ª Parte------------------

        # ------- Desenho do Cabeçalho---------------
        pdf.setFont(psfontname="Helvetica-Bold", size=12)
        pdf.setFillColor(aColor=black)
        pdf.drawString(x=2*cm, y=27*cm, text='Nome Completo: ')

        # ------- Desenho da linha abaixo do Cabeçalho
        pdf.setStrokeColor(aColor=royalblue)  # Linha Azul
        pdf.line(x1=2*cm, y1=26.8*cm, x2=6.5*cm, y2=26.8*cm)

        # ----Funcionando outras opções----#
        # texto = str(Contact.objects.filter(pk=1).get())
        # texto = str(Contact.objects.all().first())
        # texto = Contact.objects.all().order_by('first_name')
        # texto = Contact.objects.all().order_by('-first_name')  # ordem inversa
        # textobject = pdf.beginText(x=2*cm, y=26*cm)
        # textobject.setFont(psfontname="Helvetica-Oblique", size=14)
        # textobject.setFillColor(aColor=gold)
        # for nome in texto:
        #     textobject.textLines(stuff=str(nome), trim=1)

        # ------ Configuração e Desenho do Objeto ---------

        # -------- Desenho da Lista de Pessoas do Model----
        texto = Contact.objects.all()
        textobject = pdf.beginText(x=2*cm, y=26*cm)
        textobject.setFont(psfontname="Helvetica-Oblique", size=14)
        textobject.setFillColor(aColor=gold)
        for pessoa in texto:
            textobject.textLines(stuff=str(pessoa), trim=1)
        pdf.drawText(aTextObject=textobject)

        # ------------------2ª Parte------------------------

        # --------- Configuração do 2º Cabeçalho---------
        pdf.setFont(psfontname="Courier-Bold", size=14)
        pdf.setFillColor(aColor=green)
        pdf.drawString(x=2 * cm, y=14 * cm, text='Idade menor que: ')

        # --------- Desenho da linha abaixo do Cabeçalho -------
        pdf.setStrokeColor(aColor=red)  # Linha Vermelha
        pdf.line(x1=2 * cm, y1=13.8 * cm, x2=8 * cm, y2=13.8 * cm)

        # --------- Elaboração do Filtro ---------------
        idade = Contact.objects.filter(age__lt=19)
        idadeobject = pdf.beginText(x=2*cm, y=13*cm)

        # --------- Desenho das pessoas que atendem ao filtro----
        for i in idade:
            idadeobject.textLines(stuff=str(i), trim=1)
        pdf.setFillColor(aColor=blue)
        pdf.drawText(aTextObject=idadeobject)

        # --------- Apresentação Final do PDF -------------------
        pdf.showPage()
        pdf.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=False, filename='index.pdf')


# -------Exemplo com Draw String que configura dentro dela------------
def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(x=100, y=400, text="JC9.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='some.pdf')


# -------View que configura dentro dela utilizando Model -----------------
def some_view2(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="somefilename.pdf"'

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = Canvas(response)

    # ----Configuração do Título ----#
    p.setTitle(title="Clientes")
    p.setAuthor(author="JC9")

    # --- Configuração da Linha -----#
    p.setStrokeColor(aColor=blue)
    p.line(x1=2 * cm, y1=27.8 * cm, x2=7 * cm, y2=27.8 * cm)

    # --- Configuração do Texto -----#
    p.setFillColorRGB(r=0.5, g=0.2, b=1)
    p.setFont(psfontname="Helvetica-Bold", size=14)
    p.drawString(x=2*cm, y=28*cm, text='Clientes:')

    # --- Configuração do Objeto Texto ---#
    textobject = p.beginText()
    textobject.setTextOrigin(x=2*cm, y=27*cm)
    textobject.setFont(psfontname="Helvetica", size=14)

    # ---- Configuração Model ------------#
    contato = Contact.objects.filter(pk=1).get()
    nome = contato.first_name
    sobrenome = contato.last_name
    idade = contato.age
    textobject.textLines(stuff=f'Nome: {nome} \n'
                               f'Sobrenome: {sobrenome} \n'
                               f'Idade: {idade}')
    p.drawText(aTextObject=textobject)

    # --- Mostra o página ---#
    p.showPage()

    # --- Salve o arquivo e retorne o response ----#
    p.save()
    return response


# --------------------------- Weasy Print 1------------------------------#
def some_view3(request):
    HTML('http://weasyprint.org/').write_pdf('/tmp/weasyprint-website.pdf')


# --------------------------- Weasy Print 2------------------------------#
# View usando WeasyPrint, não funcionaou por falta da biblioteca libcairo
# class PDFView2(View):
#     def get(self, request, *args, **kwargs):
#         texto = ['geek university', 'texto 2', 'texto 3']
#         html_string = render_to_string('relaorio.html', {'texto': texto})
#         html = HTML(string=html_string)
#         html.write_pdf(target='/tmp/relatorio2.pdf')
#         fs = FileSystemStorage('/tmp')
#         with fs.open('relatorio2.pdf') as pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             # response['Content-Disposition'] = 'attachment; filename="relatoio2.pdf"'
#             response['Content-Disposition'] = 'inline; filename="relatoio2.pdf"'
#         return response
