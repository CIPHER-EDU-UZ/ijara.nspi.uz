# Generated by Django 4.2.4 on 2023-08-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='Holati',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Ijara holati'),
        ),
        migrations.AlterField(
            model_name='home',
            name='Ijarachi',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Ijarachining ismi'),
        ),
        migrations.AlterField(
            model_name='home',
            name='Mahallasi',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Mahalla nomi'),
        ),
        migrations.AlterField(
            model_name='home',
            name='Manzil',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Manzili'),
        ),
        migrations.AlterField(
            model_name='home',
            name='Qiz',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Qizlar uchun'),
        ),
        migrations.AlterField(
            model_name='home',
            name='Shahar',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Shahar nomi'),
        ),
        migrations.AlterField(
            model_name='home',
            name='Telefon',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Telefon raqami'),
        ),
        migrations.AlterField(
            model_name='home',
            name='Yigit',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Yigitlar uchun'),
        ),
    ]