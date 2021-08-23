from django.shortcuts import HttpResponse
from .printing import MyPrint
from io import BytesIO


def print_users(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="myuser.pdf"'

    buffer = BytesIO()

    report = MyPrint(buffer, 'A4')
    pdf = report.print_users()

    response.write(pdf)
    return response
