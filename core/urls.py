from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home_list'),
    path('create/', create_ariza, name='create_ariza'),
    path('ariza/<slug:unique_id>/', ariza_detail_view, name='ariza_detail'),
    path('approve/<slug:unique_id>/', approve_ariza, name='approve_ariza'),
    path('check_status/', check_status, name='check_status'),
    path('test/', test, name='test'),
    path('upload/', upload_excel, name='upload_excel'),
]


handler404 = 'core.views.custom_404_view'