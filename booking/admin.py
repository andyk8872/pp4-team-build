from django.contrib import admin
from .models import Booking, Review


@admin.register(Booking)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_no_group', 'creation_date', 'approved')
    list_filter = ('approved', 'booking_date')
    search_fields = ('contact_name', 'booking_date')


@admin.register(Review)
class Review(admin.ModelAdmin):

    list_display = ('user', 'creation_date', 'review', 'approved')
