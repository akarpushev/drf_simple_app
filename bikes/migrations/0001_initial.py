# Generated by Django 4.2.11 on 2024-08-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('available', 'Available'), ('rented', 'Rented')], max_length=50)),
            ],
        ),
    ]
