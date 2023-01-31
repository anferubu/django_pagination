from django.urls import path

from .views import ContactList


app_name = 'contact'

urlpatterns = [
    path('', ContactList.as_view(), name='list'),
]