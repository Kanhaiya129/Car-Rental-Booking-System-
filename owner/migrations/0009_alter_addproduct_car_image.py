# Generated by Django 4.1.5 on 2023-02-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0008_addproduct_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
