from django.urls import path

from .views import *

urlpatterns = [
    path("", home_list_view, name="home"),
    path('upload/', upload_excel, name='upload_excel'),
    path('test/', test, name='test')
]