# Generated by Django 4.1.5 on 2023-01-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_boookedcardetail_car_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='boookedcardetail',
            name='per_day_rent',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
    ]
