# Generated by Django 3.0.5 on 2021-10-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0017_auto_20211008_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='firstapp/productimages'),
        ),
    ]
