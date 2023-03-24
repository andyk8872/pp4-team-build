from .models import Booking, Review
from django import forms
import datetime


class DateInput(forms.DateInput):
    """
    Class to make a calender showing when choosing the date.
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """
    Presents the form with the fields and widgets/validators.
    """
    class Meta:
        model = Booking
        fields = ('contact_name',
                  'email',
                  'phone',
                  'total_no_group',
                  'activity_type',
                  'booking_date',)
        widgets = {
            'booking_date': DateInput(attrs={
                'required': True,
                'min': datetime.date.today()+datetime.timedelta(days=2),
                'max': datetime.date.today()+datetime.timedelta(days=60)}),
            'email': forms.EmailInput(attrs={
                'required': True}),
            'phone': forms.TextInput(attrs={
                'required': True}),
            'contact_name': forms.TextInput(attrs={
                'required': True,
            })
                }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('review',)

        widgets = {
            'review': forms.Textarea(attrs={
                'required': True,
            })
                }
