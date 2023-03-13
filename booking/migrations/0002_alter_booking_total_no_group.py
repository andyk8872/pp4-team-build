# Generated by Django 3.2.18 on 2023-03-13 18:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_no_group',
            field=models.IntegerField(blank=True, default=10, null=True, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(10)], verbose_name='No. in Group (Min 10, Max = 30)'),
        ),
    ]