from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_name',
        'student_lastnem',
        'student_surname',
        'student_brithday',  
        'student_state',
        'student_region',
        'student_tuman',
        'student_pasport',
        'student_pasportint',
        'student_adress',
        'student_fakultet',
        'student_kurs',
        'student_phone',

        )
admin.site.register(Stuudents, StudentAdmin)

class AdminUy(admin.ModelAdmin):
    list_display = (
        'Manzil', 
        'Xonalar',
        'Yotoqlar',
        'GENDER_CHOICES',
        'location',
        'price',
        'room_size',
        'number_of_rooms',
        'number_of_beds',
        'gender',
        'kitchen',
        'tv',
        'wifi',
        'balcony',
        'garage',
        'bathroom',
        'washing_machine',
        'refrigerator',
        'area_of_house',
        'proximity_to_university',
        'proximity_to_public_transportation',
    )
admin.site.register(IjaraUy, AdminUy)
admin.site.register(Yotoqxona)