# Generated by Django 4.0.5 on 2022-06-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_locationdatetime_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationdatetime',
            name='slots',
            field=models.PositiveBigIntegerField(),
        ),
    ]
