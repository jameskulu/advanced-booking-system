# Generated by Django 4.0.5 on 2022-06-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_locationdatetime_slots'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slots', models.PositiveBigIntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='locationdatetime',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='locationdatetime',
            name='date',
        ),
        migrations.RemoveField(
            model_name='locationdatetime',
            name='location',
        ),
        migrations.RemoveField(
            model_name='locationdatetime',
            name='time',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]
