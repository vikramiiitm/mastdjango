# Generated by Django 3.0.5 on 2021-10-02 10:36

from django.db import migrations, models
import firstapp.models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_auto_20211002_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=firstapp.models.LowercaseEmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Seller', 'SELLER'), ('Customer', 'CUSTOMER')], default=[], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Not Packed'), (2, 'Ready For Shipment'), (4, 'Delivered'), (3, 'Shipped')], default=1),
        ),
    ]
