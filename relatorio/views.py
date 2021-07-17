# ReportLab
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import blue, black, green, gold, rosybrown, red, royalblue

# WeasyPrint
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML

from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from relatorio.models import Contact


class ContactListView(ListView):
    model = Contact


class ContactDetailView(DetailView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# -------------------- ReportLab ---------------------------#
class PDFView(View):

    @staticmethod
    def get(request, *args, **kwargs):

        # ------- Configuração Inicial-------
        buffer = io.BytesIO()
        pdf = Canvas(buffer)

        # ------- Nome Completo -------------

        pdf.setFont(psfontname="Helvetica-Bold", size=12)
        pdf.setFillColor(aColor=black)
        pdf.drawString(x=2*cm, y=27*cm, text='Nome Completo: ')

        pdf.setStrokeColor(aColor=royalblue)
        pdf.line(x1=2*cm, y1=26.8*cm, x2=6.5*cm, y2=26.8*cm)

        # texto = str(Contact.objects.filter(pk=1).get())
        # texto = str(Contact.objects.all().values())
        # texto = str(Contact.objects.all().values_list())
        # texto = str(Contact.objects.all())
        # texto = str(Contact.objects.all().first())

        texto = Contact.objects.all().order_by('first_name')
        # texto = Contact.objects.all().order_by('-first_name') # ordem inversa

        textobject = pdf.beginText(x=2*cm, y=26*cm)
        textobject.setFont(psfontname="Helvetica-Oblique", size=14)
        textobject.setFillColor(aColor=gold)

        # textobject.textLines(stuff=texto, trim=1)
        for nome in texto:
            textobject.textLines(stuff=str(nome), trim=1)

        pdf.drawText(aTextObject=textobject)

        # -------- Idade -------------#
        pdf.setFont(psfontname="Courier-Bold", size=14)
        pdf.setFillColor(aColor=green)
        pdf.drawString(x=2 * cm, y=23 * cm, text='Idade menor que 50: ')

        pdf.setStrokeColor(aColor=red)
        pdf.line(x1=2 * cm, y1=22.8 * cm, x2=8 * cm, y2=22.8 * cm)

        idade = Contact.objects.filter(age__lt=50)

        idadeobject = pdf.beginText(x=2*cm, y=22*cm)
        pdf.setFillColor(aColor=blue)

        for i in idade:
            idadeobject.textLines(stuff=str(i), trim=1)
        pdf.drawText(aTextObject=idadeobject)

        # ---- Apresentação Final do PDF --------
        pdf.showPage()
        pdf.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=False, filename='index.pdf')


def some_view3(request):
    HTML('http://weasyprint.org/').write_pdf('/tmp/weasyprint-website.pdf')


# --------------------- ReportLab -------------------------- #
def some_view2(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="somefilename.pdf"'

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = Canvas(response)

    # --- Texto Objeto -----#
    p.setFont(psfontname="Helvetica", size=14)
    # p.setStrokeColor(aColor=blue)
    p.setFillColorRGB(r=0.5, g=0.2, b=1)
    p.drawString(x=2*cm, y=27*cm, text='Nome: ')
    textobject = p.beginText()
    textobject.setTextOrigin(x=3.5 * cm, y=27 * cm)
    textobject.setFont(psfontname="Helvetica", size=14)
    textobject.setStrokeColor(aColor=blue)
    contato = Contact.objects.filter(pk=2).get()
    nome = contato.first_name
    sobrenome = contato.last_name
    textobject.textLines(stuff=nome + " " + sobrenome)
    p.drawText(aTextObject=textobject)

    # Mostre o Objeto
    p.showPage()
    # Salve o arquivo e retorne o response
    p.save()
    return response


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "JC9.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='some.pdf')


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
