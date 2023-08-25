from django.db import models
from django.utils.crypto import get_random_string
import uuid

class Test(models.Model):
    t_image = models.ImageField(upload_to='ijara/')

<<<<<<< HEAD
class Yotoqxonalar(models.Model):
    name = models.CharField(max_length=150, verbose_name='Yotoqxona nomi')
    image= models.ImageField(upload_to='yotoqxona/')
    sigm = models.IntegerField(verbose_name='Yotoqxona sig\'imi')
    about = models.CharField(max_length=150, verbose_name='Yotoqxona xaqida')
    def __str__(self):
        return self.name
=======
>>>>>>> 3ce5759c8b8da84a6cbcd2ad68b082be7e53ef04
class Home(models.Model):
    Shahar = models.CharField(max_length=150, verbose_name='Shahar nomi', null=True,)
    Mahallasi = models.CharField(max_length=150, verbose_name='Mahalla nomi', null=True,)
    Manzil = models.CharField(max_length=150, verbose_name='Manzili', null=True,)
    Ijarachi = models.CharField(max_length=150, verbose_name='Ijarachining ismi', null=True,)
    Telefon = models.CharField(max_length=150, verbose_name='Telefon raqami', null=True,)
    Yigit = models.CharField(max_length=150, verbose_name='Yigitlar uchun', null=True,)
    Qiz = models.CharField(max_length=150, verbose_name='Qizlar uchun', null=True,)
    Holati = models.CharField(max_length=150, verbose_name='Ijara holati', null=True,)

    def __str__(self):
        if self.Shahar is not None:
            return self.Shahar
        return "Record with no specified Shahar"
    

class Ariza(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ism = models.CharField(max_length=15, verbose_name="Ismi",  null=False, unique=True)
    familiya = models.CharField(max_length=20, verbose_name='Familiyasi', null=False, )
    sharifi = models.CharField(max_length=20, verbose_name='Otasining ismi', null=False)
    mamlakat_choice = [
        ('uzbekistan', 'O\'zbekistan'),
        ('india', 'India'),
        ('kazakhstan', 'Kazakhstan'),
        ('kyrgyzstan', 'Kyrgyzstan'),
        ('tajikistan', 'Tajikistan'),
        ('afganistan', 'Afganistan'),
    ]
    mamlakat = models.CharField(max_length=100, choices=mamlakat_choice, verbose_name='Region', blank=False)
    viloyat_choice  = [
        ('tashkent', 'Tashkent'),
        ('samarkand', 'Samarkand'),
        ('bukhara', 'Bukhara'),
        ('andijan', 'Andijan'),
        ('ferghana', 'Ferghana'),
        ('namangan', 'Namangan'),
        ('navoiy', 'Navoiy'),
        ('surkhandarya', 'Surkhandarya'),
        ('jizzakh', 'Jizzakh'),
        ('kashkadarya', 'Kashkadarya'),
        ('sirdaryo', 'Sirdaryo'),
        ('khorezm', 'Khorezm'),
        ('karakalpakstan', 'Karakalpakstan'),
    ]
    viloyat = models.CharField(max_length=100, choices=viloyat_choice, verbose_name='Region', null=False)
    tuman = models.CharField(max_length=30, verbose_name="Tuman nomini kriting", null=False)
    jinsi_choice = [
        ('erkak', 'Erkak'),
        ('ayol', 'Ayol'),
    ]
    jinsi = models.CharField(max_length=15, choices=jinsi_choice, verbose_name='Jinsini tanlang', null=False)
    pasport = models.CharField(max_length=2, verbose_name="pasport seriya", unique=True)
    pasport_num = models.IntegerField(verbose_name="Pasport raqami", unique=True)
    manzil = models.CharField(max_length=150, verbose_name='Yashash manzili')
    fakulte_choices = [
        ('matematika va informatika', 'Matematika va Informatika'),
        ('rus va qozoq filialogiyasi', 'Rus va Qozoq filialogiyasi'),
        ('tarix', 'Tarix'),
        ('ingliz tili va adabioti', 'Ingliz tili va Adabioti'),
        ('jismoniy madaniyat', 'Jismoniy Madaniyat'),
        ('sa\'atshunoslik', 'Sa\'atshunoslik'),
        ('tibbiyot', 'Tibbiyot'),
    ]

    fakultet = models.CharField(max_length=150, choices=fakulte_choices, verbose_name='Fakultetni tanlang', null=False)
    yunalish = models.CharField(max_length=150, verbose_name="yunalishni kriting")
    grux = models.CharField(max_length=30,  verbose_name='grux nomi')
    kurs_choice = [
        ('1kurs', '1 Kurs'),
        ('2kurs', '2 Kurs'),
        ('3kurs', '3 Kurs'),
        ('4kurs', '4 Kurs'),
    ]
    kurs = models.CharField(max_length=15, choices=kurs_choice, verbose_name='kursni tanlang', null=False)
    telefon = models.IntegerField(verbose_name='Telefon raqam', unique=True)
    uploaded_file = models.FileField(upload_to='xujjatlar/')
    
    unique_id = models.CharField(max_length=10, unique=True, editable=False,)
    comments = models.TextField(blank=True, verbose_name='Comments')
    # is_approved = models.BooleanField(default=False, verbose_name='Is Approved')

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = get_random_string(length=10)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ism
    
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

        ('1 xona', '1 xona'),
        ('2 xona', '2 xona'),
        ('3 xona', '3 xona'),
        ('4 xona', '4 xona'),

    ]
    Yotoqlar =[ 

        ('1 yotoq', '1 yotoq'),
        ('2 yotoq', '2 yotoq'),
        ('3 yotoq', '3 yotoq'),
        ('4 yotoq', '4 yotoq'),

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


# class Yotoqxona(models.Model):
#     yotoqxona_name = models.CharField(max_length=150, verbose_name="Yotoqxona nomi")
#     yotoqxona_rooms = models.IntegerField(verbose_name="Yotoqona xonalari")
#     yotoqxona_type = models.CharField(max_length=10, choices=[('girl', 'Girl'), ('boy', 'Boy')])

#     def __str__(self):
#         return self.yotoqxona_name

# class 
# class Yotoqxona_bron(models.Model):

#    yotoqxona_name = models.ForeignKey(Yotoqxona, on_delete=models.CASCADE, verbose_name='Yotoqxona nomi')
   