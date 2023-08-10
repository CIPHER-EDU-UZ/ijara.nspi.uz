from django.db import models

class Stuudents(models.Model):
    student_name = models.CharField(max_length=25, verbose_name="Student ismi")
    student_lastnem = models.CharField(max_length=25, verbose_name="Student familiyasi")
    student_surname = models.CharField(max_length=25, verbose_name="Student otasining ismi")
    student_brithday = models.DateTimeField(verbose_name="Tug'ilgan kuni")
    student_state = models.CharField(max_length=150, verbose_name="Tug'ilgan davlati")
    student_region = [
        ('Andijon viloyati', 'Andijon viloyati'),
        ('Buxoro viloyati', 'Buxoro viloyati'),
        ('Jizzax viloyati', 'Jizzax viloyati'),
        ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'),
        ('Navoiy viloyati', 'Navoiy viloyati'),
        ('Namangan viloyati', 'Namangan viloyati'),
        ('Samarqand viloyati', 'Samarqand viloyati'),
        ('Suraxandaryo viloyati', 'Suraxandaryo viloyati'),
        ('Sirdaryo viloyati', 'Sirdaryo viloyati'),
        ('Toshkent viloyati', 'Toshkent viloyati'),
        ('Farg\'ona viloyati', 'Farg\'ona viloyati'),
        ('Xorazm viloyati', 'Xorazm viloyati'),
        ('Toshkent shahar', 'Toshkent shahar'),
    ]

    student_tuman = models.CharField(max_length=150, verbose_name='Tuman nomini kriting')
    student_pasport = models.CharField(max_length=2, verbose_name="Pasport seriya")
    student_pasportint = models.IntegerField(verbose_name="Pasport seriyasi")
    student_adress = models.CharField(max_length=150, verbose_name='Yashash manzili')
    student_fakultet = [
        ('Informatika fanlar',  'Informatika fanlar'),
        ('Tabiiy fanlar',  'Tabiiy fanlar'),
        ('Tarix ',  'Tarix'),
        ('Ingliz tili va Adabiyoti',  'Ingliz tili va Adabiyoti'),
        ('Sa\'tshunoslik',  'Sa\'tshunoslik'),
        ('Rus va Qozoq filialogiyasi',  'Rus va Qozoq filialogiyasi'),
        ('Jismoniy madaniyat',  'Jismoniy madaniyat'),
        ('Maktabgaca va Boshlang\'ch ta\'lim ',  'Maktabgaca va Boshlang\'ch ta\'lim'),
        ('Fizika va Texnologiyalar',  'Fizika va Texnologiyalar'),
        ('O\'zbek tili va Adabiyoti',  'O\'zbek tili va Adabiyoti'),
    ]

    student_kurs = [

        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),

    ]

    student_phone = models.IntegerField(verbose_name='Telefon raqami')
# end student register

class IjaraUy(models.Model):
    Manzil = [

        ('Shaxar markazi', 'Shaxar markazi'),
        ('Shahar chekkasi', 'Shahar chekkasi'),
        ('Oliygoh yaqinida', 'Oliygoh yaqinida'),

    ]
    Xonalar = [

        (1, '1 xona'),
        (2, '2 xona'),
        (3, '3 xona'),
        (4, '4 xona'),

    ]
    Yotoqlar =[ 

        (1, '1 yotoq'),
        (2, '2 yotoq'),
        (3, '3 yotoq'),
        (4, '4 yotoq'),

    ]
    GENDER_CHOICES = [

        ('boys', 'Yigitlar'),
        ('girls', 'Qizlar'),
        ('mixed', 'Aralash'),

    ]
    location = models.CharField(max_length=100, choices=Manzil)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    room_size = models.PositiveIntegerField()
    number_of_rooms = models.CharField(choices=Xonalar,max_length=150,  verbose_name='Xonalar Soni')
    number_of_beds = models.CharField( choices=Yotoqlar,max_length=150,  verbose_name='Yotoqlar soni')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=150, verbose_name='Kim uchun' )
    kitchen = models.BooleanField(default=False, verbose_name='Oshxona')
    tv = models.BooleanField(default=False, verbose_name=('Televizior'))
    wifi = models.BooleanField(default=False, verbose_name=('Wifi'))
    balcony = models.BooleanField(default=False, verbose_name=('Balkon'))
    garage = models.BooleanField(default=False, verbose_name=('Garaj'))
    bathroom = models.BooleanField(default=False,  verbose_name=('Hammom'))
    washing_machine = models.BooleanField(default=False, verbose_name=('Kir yuvish mashinasi'))
    refrigerator = models.BooleanField(default=False,verbose_name=('Konditsioner'))
    area_of_house = models.DecimalField(max_digits=6, decimal_places=2)
    proximity_to_university = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Oliygohga_yaqinligi')
    proximity_to_public_transportation = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='jamoat_transportiga_yaqinlik')

    def __str__(self):
        return f"{self.location} - {self.pk}"


class Yotoqxona(models.Model):
    yotoqxona_name = models.CharField(max_length=150, verbose_name="Yotoqxona nomi")
    yotoqxona_rooms = models.IntegerField(verbose_name="Yotoqona xonalari")
    yotoqxona_type = models.CharField(max_length=10, choices=[('girl', 'Girl'), ('boy', 'Boy')])

# class Yotoqxona_bron(models.Model):

#    yotoqxona_name = models.ForeignKey(Yotoqxona, on_delete=models.CASCADE, verbose_name='Yotoqxona nomi')
   