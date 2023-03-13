from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
import datetime
from datetime import timedelta, date


class Booking(models.Model):

    ACTIVITY_LIST = (
        ('Team Building Workshop', 'Team Building Workshop'),
        ('Carnival Team Challenge', 'Carnival Team Challenge'),
        ('Bridge Building Challeng', 'Bridge Building Challenge'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User name'),
        related_name='bookings',
        blank=True, null=True)

    contact_name = models.CharField(
        verbose_name=_('Contact name'),
        max_length=20,
        blank=True)

    email = models.EmailField(
        verbose_name=_('Email'),
        blank=True)

    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=256,
        blank=True)

    creation_date = models.DateTimeField(
        verbose_name=_('Creation date'),
        auto_now_add=True)

    total_no_group = models.IntegerField(
        verbose_name=('No. in Group (Min 10, Max = 30)'),
        default=10,
        validators=[
            MaxValueValidator(30),
            MinValueValidator(10)
        ],
        blank=True, null=True)

    activity_type = models.CharField(
        verbose_name=_('Activity Type'),
        default='BBC',
        max_length=256,
        choices=ACTIVITY_LIST)

    booking_date = models.DateField(
        verbose_name=_('Booking date'),
        blank=True, null=True, unique=True,
        validators=[MinValueValidator(date.today() + timedelta(days=2))])

    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return (str(self.user))
