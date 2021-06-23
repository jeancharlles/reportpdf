from django.urls import path
from relatorio.views import some_view, some_view2, IndexView, ContactListView, ContactDetailView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    # path('index2', IndexView2.as_view(), name='index2'),
    path('some/', some_view, name='some'),
    path('some2/', some_view2, name='some2'),
    path('contact-list/', ContactListView.as_view(), name='contact-list'),
    path('contact-detail/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]
