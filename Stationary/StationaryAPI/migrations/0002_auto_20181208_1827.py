# Generated by Django 2.1.4 on 2018-12-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StationaryAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='DeliveryDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='supplyorder',
            name='DeliveryDate',
            field=models.DateField(null=True),
        ),
    ]
