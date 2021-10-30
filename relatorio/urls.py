from django.urls import path
from relatorio.views import *

urlpatterns = [
    path('pdf/', PDFView.as_view(), name='pdf'),
    # path('index2', IndexView2.as_view(), name='index2'),

    path('', IndexView.as_view(), name='index'),
    path('some/', some_view, name='some'),
    path('some2/', some_view2, name='some2'),
    path('some3/', some_view3, name='some3'),

    path('reportpdf/', reportpdf, name='reportpdf'),
    path('reportpdfpage/', reportpdfpage, name='reportpdfpage'),

    path('lista/', lista, name='lista'),

    path('contact-list/', ContactListView.as_view(), name='contact-list'),

    path('contact-detail/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),

    path('contact-detailpdf/<int:pk>/', detail_pdf, name='contact-detailpdf'),

    path('contact-detailpdf2/<int:pk>/', detail_pdf2, name='contact-detailpdf2'),
]
