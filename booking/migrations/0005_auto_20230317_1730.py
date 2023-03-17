# Generated by Django 3.2.18 on 2023-03-17 17:30

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20230316_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(datetime.date(2023, 3, 19))], verbose_name='Booking date'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(blank=True, default=''),
        ),
    ]
