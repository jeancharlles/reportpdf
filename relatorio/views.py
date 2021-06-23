
# ReportLab
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# WeasyPrint
# from django.core.files.storage import FileSystemStorage
# from django.template.loader import render_to_string
# from django.http import HttpResponse
# from weasyprint import HTML

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


class IndexView(View):  # ReportLab
    @staticmethod
    def get(request, *args, **kwargs):
        # Cria um arquivo para receber os dados e gerar o pdf
        buffer = io.BytesIO()

        # Criar o arquivo pdf
        pdf = canvas.Canvas(buffer)

        # Parametros a serem utilizados
        pdf.translate(inch, inch)
        pdf.setFont(psfontname="Helvetica-Oblique", size=14)
        pdf.setAuthor(author='Jean')
        pdf.addPageLabel(pageNum=1)
        pdf.drawString(0, 0, text='JC9 1')

        # Quado acabamos de inserir os parâmetros no pdf
        pdf.showPage()

        pdf.save()

        # Por fim, retornamos o buffer para o início do arquivo
        buffer.seek(0)

        return FileResponse(buffer, as_attachment=False, filename='index1.pdf')


def some_view2(request):  # ReportLab
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="somefilename.pdf"'

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = canvas.Canvas(response)

    # Desenhe coisas no PDF. Aqui é onde a geração do PDF acontece.
    # Veja a documentação do ReportLab para a lista completa de
    # funcionalidades.
    p.drawString(100, 100, "JC9 2")

    # Mostre o Objeto
    p.showPage()

    # Salve o arquivo e retorne o response
    p.save()
    return response


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

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
# class IndexView2(View):
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
