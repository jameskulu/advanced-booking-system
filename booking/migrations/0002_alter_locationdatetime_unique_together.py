# Generated by Django 4.0.5 on 2022-06-27 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locationdatetime',
            unique_together={('location', 'date', 'time')},
        ),
    ]
