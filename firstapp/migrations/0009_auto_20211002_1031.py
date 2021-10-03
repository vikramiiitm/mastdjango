# Generated by Django 3.0.5 on 2021-10-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_auto_20211002_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(2, 'Ready For Shipment'), (3, 'Shipped'), (4, 'Delivered'), (1, 'Not Packed')], default=1),
        ),
    ]