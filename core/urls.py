from django.urls import path
from .views import *
urlpatterns = [
    path('', room_list, name='room_list'),
    path('room/<int:room_id>/', student_list, name='student_list'),

]
