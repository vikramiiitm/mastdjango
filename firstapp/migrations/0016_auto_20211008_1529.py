# Generated by Django 3.0.5 on 2021-10-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0015_auto_20211002_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='firstapp/productimages'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(4, 'Delivered'), (2, 'Ready For Shipment'), (3, 'Shipped'), (1, 'Not Packed')], default=1),
        ),
    ]