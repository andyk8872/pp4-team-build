from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class HomePage(TemplateView):
    template_name = "index.html"


class ContactPage(TemplateView):
    template_name = "contact.html"


@login_required
def make_booking(request):

    if request.method == 'POST':
        booking = Booking(user=request.user)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking successful.\
                 Please allow up to 24 hours to finalise details/payment.')
            return redirect('my_account')
    else:
        form = BookingForm()
    return render(request, 'make_booking.html', {'form': form})


@login_required
def view_booking(request):

    bookings = request.user.bookings.all()
    context = {
        'bookings': bookings,
    }
    return render(request, 'my_account.html', context)


@login_required
def edit_booking(request, booking_id):
    try:
        booking = get_object_or_404(Booking, id=booking_id)
        if request.method == 'POST':
            form = BookingForm(request.POST, instance=booking)
            if form.is_valid():
                form.save()
                messages.success(request, 'Update successful..\
                 We will follow up within 24 hours to finalise details &\
                     payment.')
                return redirect('my_account')
        else:
            form = BookingForm(instance=booking)
        context = {
                 'form': form
        }
        return render(request, 'edit_booking.html', context)

    except Http404 as err:
        return redirect('my_account')


@login_required
def delete_booking(request, booking_id):
    item = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Booking delete successful..')
        return redirect('my_account')
    context = {
        "booking": item
    }    
    return render(request, "delete_items.html", context)
