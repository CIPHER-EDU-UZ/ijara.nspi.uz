from django.urls import path

from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path('upload/', upload_excel, name='upload_excel'),
    path('test/', test, name='test')
]