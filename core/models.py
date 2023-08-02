from django.db import models

# class IjaraUy(models.Model):
#     Manzil = [
#         ('Shaxar markazi', 'Shaxar markazi'),
#         ('Shahar chekkasi', 'Shahar chekkasi'),
#         ('Oliygoh yaqinida', 'Oliygoh yaqinida'),
#     ]
#     Xonalar = [
#         (1, '1 xona'),
#         (2, '2 xona'),
#         (3, '3 xona'),
#         (4, '4 xona'),
#         # Add more options if needed
#     ]
#     Yotoqlar =[ 
#         (1, '1 yotoq'),
#         (2, '2 yotoq'),
#         (3, '3 yotoq'),
#         (4, '4 yotoq'),
#         # Add more options if needed
#     ]
#     GENDER_CHOICES = [
#         ('boys', 'Yigitlar'),
#         ('girls', 'Qizlar'),
#         ('mixed', 'Aralash'),
#     ]
#     location = models.CharField(max_length=100, choices=Manzil)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     room_size = models.PositiveIntegerField()
#     number_of_rooms = models.CharField(choices=Xonalar,max_length=150,  verbose_name='Xonalar Soni')
#     number_of_beds = models.CharField( choices=Yotoqlar,max_length=150,  verbose_name='Yotoqlar soni')
#     gender = models.CharField(choices=GENDER_CHOICES, max_length=150, verbose_name='Kim uchun' )
#     kitchen = models.BooleanField(default=False, verbose_name='Oshxona')
#     tv = models.BooleanField(default=False, verbose_name=('Televizior'))
#     wifi = models.BooleanField(default=False, verbose_name=('Wifi'))
#     balcony = models.BooleanField(default=False, verbose_name=('Balkon'))
#     garage = models.BooleanField(default=False, verbose_name=('Garaj'))
#     bathroom = models.BooleanField(default=False,  verbose_name=('Hammom'))
#     washing_machine = models.BooleanField(default=False, verbose_name=('Kir yuvish mashinasi'))
#     refrigerator = models.BooleanField(default=False,verbose_name=('Konditsioner'))
#     area_of_house = models.DecimalField(max_digits=6, decimal_places=2)
#     proximity_to_university = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Oliygohga_yaqinligi')
#     proximity_to_public_transportation = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='jamoat_transportiga_yaqinlik')

#     def __str__(self):
#         return f"{self.location} - {self.pk}"

class Room(models.Model):
    name = models.CharField(max_length=100)
    max_seats = models.PositiveIntegerField(default=6)

    @property
    def reserved_seats(self):
        return self.students.count()

class Student(models.Model):
    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
