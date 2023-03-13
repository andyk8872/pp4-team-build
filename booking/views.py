from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class HomePage(TemplateView):
    template_name = "index.html"


@login_required
def make_booking(request):

    if request.method == 'POST':
        booking = Booking(user=request.user)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'make_booking.html', {'form': form})  
