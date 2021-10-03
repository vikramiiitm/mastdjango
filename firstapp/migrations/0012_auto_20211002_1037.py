# Generated by Django 3.0.5 on 2021-10-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_auto_20211002_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(4, 'Delivered'), (1, 'Not Packed'), (2, 'Ready For Shipment'), (3, 'Shipped')], default=1),
        ),
    ]