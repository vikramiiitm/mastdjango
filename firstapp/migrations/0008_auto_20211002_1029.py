# Generated by Django 3.0.5 on 2021-10-02 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_auto_20211002_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(2, 'Ready For Shipment'), (1, 'Not Packed'), (4, 'Delivered'), (3, 'Shipped')], default=1),
        ),
    ]
