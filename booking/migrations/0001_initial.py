# Generated by Django 3.2.18 on 2023-03-13 09:54

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=20, verbose_name='Contact name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=256, verbose_name='Phone')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('total_no_group', models.IntegerField(blank=True, default=10, null=True, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(10)], verbose_name='No. in Group(Min 10, Max = 30)')),
                ('activity_type', models.CharField(choices=[('Team Building Workshop', 'Team Building Workshop'), ('Carnival Team Challenge', 'Carnival Team Challenge'), ('Bridge Building Challeng', 'Bridge Building Challenge')], default='BBC', max_length=256, verbose_name='Activity Type')),
                ('booking_date', models.DateField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(datetime.date(2023, 3, 15))], verbose_name='Booking date')),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL, verbose_name='User name')),
            ],
            options={
                'ordering': ['creation_date'],
            },
        ),
    ]