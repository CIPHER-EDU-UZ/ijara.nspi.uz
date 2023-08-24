# Generated by Django 4.2.4 on 2023-08-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ariza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=15, unique=True, verbose_name='Ismi')),
                ('familiya', models.CharField(max_length=20, verbose_name='Familiyasi')),
                ('sharifi', models.CharField(max_length=20, verbose_name='Otasining ismi')),
                ('mamlakat', models.CharField(choices=[('uzbekistan', "O'zbekistan"), ('india', 'India'), ('kazakhstan', 'Kazakhstan'), ('kyrgyzstan', 'Kyrgyzstan'), ('tajikistan', 'Tajikistan'), ('afganistan', 'Afganistan')], max_length=100, verbose_name='Region')),
                ('viloyat', models.CharField(choices=[('tashkent', 'Tashkent'), ('samarkand', 'Samarkand'), ('bukhara', 'Bukhara'), ('andijan', 'Andijan'), ('ferghana', 'Ferghana'), ('namangan', 'Namangan'), ('navoiy', 'Navoiy'), ('surkhandarya', 'Surkhandarya'), ('jizzakh', 'Jizzakh'), ('kashkadarya', 'Kashkadarya'), ('sirdaryo', 'Sirdaryo'), ('khorezm', 'Khorezm'), ('karakalpakstan', 'Karakalpakstan')], max_length=100, verbose_name='Region')),
                ('tuman', models.CharField(max_length=30, verbose_name='Tuman nomini kriting')),
                ('jinsi', models.CharField(choices=[('erkak', 'Erkak'), ('ayol', 'Ayol')], max_length=15, verbose_name='Jinsini tanlang')),
                ('pasport', models.CharField(max_length=2, unique=True, verbose_name='pasport seriya')),
                ('pasport_num', models.IntegerField(unique=True, verbose_name='Pasport raqami')),
                ('manzil', models.CharField(max_length=150, verbose_name='Yashash manzili')),
                ('fakultet', models.CharField(choices=[('matematika va informatika', 'Matematika va Informatika'), ('rus va qozoq filialogiyasi', 'Rus va Qozoq filialogiyasi'), ('tarix', 'Tarix'), ('ingliz tili va adabioti', 'Ingliz tili va Adabioti'), ('jismoniy madaniyat', 'Jismoniy Madaniyat'), ("sa'atshunoslik", "Sa'atshunoslik"), ('tibbiyot', 'Tibbiyot')], max_length=150, verbose_name='Fakultetni tanlang')),
                ('yunalish', models.CharField(max_length=150, verbose_name='yunalishni kriting')),
                ('grux', models.CharField(max_length=30, verbose_name='grux nomi')),
                ('kurs', models.CharField(choices=[('1kurs', '1 Kurs'), ('2kurs', '2 Kurs'), ('3kurs', '3 Kurs'), ('4kurs', '4 Kurs')], max_length=15, verbose_name='kursni tanlang')),
                ('telefon', models.IntegerField(unique=True, verbose_name='Telefon raqam')),
                ('uploaded_file', models.FileField(upload_to='xujjatlar/')),
                ('unique_id', models.CharField(editable=False, max_length=10, unique=True)),
                ('comments', models.TextField(blank=True, verbose_name='Comments')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Is Approved')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shahar', models.CharField(max_length=150, null=True, verbose_name='Shahar nomi')),
                ('Mahallasi', models.CharField(max_length=150, null=True, verbose_name='Mahalla nomi')),
                ('Manzil', models.CharField(max_length=150, null=True, verbose_name='Manzili')),
                ('Ijarachi', models.CharField(max_length=150, null=True, verbose_name='Ijarachining ismi')),
                ('Telefon', models.CharField(max_length=150, null=True, verbose_name='Telefon raqami')),
                ('Yigit', models.CharField(max_length=150, null=True, verbose_name='Yigitlar uchun')),
                ('Qiz', models.CharField(max_length=150, null=True, verbose_name='Qizlar uchun')),
                ('Holati', models.CharField(max_length=150, null=True, verbose_name='Ijara holati')),
            ],
        ),
        migrations.CreateModel(
            name='Stuudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=25, verbose_name='Student ismi')),
                ('student_lastnem', models.CharField(max_length=25, verbose_name='Student familiyasi')),
                ('student_surname', models.CharField(max_length=25, verbose_name='Student otasining ismi')),
                ('student_brithday', models.DateTimeField(verbose_name="Tug'ilgan kuni")),
                ('student_state', models.CharField(max_length=150, verbose_name="Tug'ilgan davlati")),
                ('student_tuman', models.CharField(max_length=150, verbose_name='Tuman nomini kriting')),
                ('student_pasport', models.CharField(max_length=2, verbose_name='Pasport seriya')),
                ('student_pasportint', models.IntegerField(verbose_name='Pasport seriyasi')),
                ('student_adress', models.CharField(max_length=150, verbose_name='Yashash manzili')),
                ('student_phone', models.IntegerField(verbose_name='Telefon raqami')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_image', models.ImageField(upload_to='ijara/')),
            ],
        ),
        migrations.CreateModel(
            name='Yotoqxona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yotoqxona_name', models.CharField(max_length=150, verbose_name='Yotoqxona nomi')),
                ('yotoqxona_rooms', models.IntegerField(verbose_name='Yotoqona xonalari')),
                ('yotoqxona_type', models.CharField(choices=[('girl', 'Girl'), ('boy', 'Boy')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='ijarauy',
            name='number_of_beds',
            field=models.CharField(choices=[('1 yotoq', '1 yotoq'), ('2 yotoq', '2 yotoq'), ('3 yotoq', '3 yotoq'), ('4 yotoq', '4 yotoq')], max_length=150, verbose_name='Yotoqlar soni'),
        ),
        migrations.AlterField(
            model_name='ijarauy',
            name='number_of_rooms',
            field=models.CharField(choices=[('1 xona', '1 xona'), ('2 xona', '2 xona'), ('3 xona', '3 xona'), ('4 xona', '4 xona')], max_length=150, verbose_name='Xonalar Soni'),
        ),
    ]
