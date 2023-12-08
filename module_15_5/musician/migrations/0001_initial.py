# Generated by Django 4.2.7 on 2023-12-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=13)),
                ('instrument_type', models.CharField(max_length=9)),
            ],
        ),
    ]
