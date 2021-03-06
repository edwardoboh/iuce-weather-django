# Generated by Django 3.2 on 2021-04-10 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SenorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(max_length=10, verbose_name='Temperature')),
                ('pressure', models.CharField(max_length=10, verbose_name='Pressure')),
                ('humidity', models.CharField(max_length=10, verbose_name='Hunidity')),
                ('light', models.CharField(max_length=10, verbose_name='Light Intensity')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
