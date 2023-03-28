from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .forms import BookingForm, ContactForm, ReviewForm
from .models import Booking, Review
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string


class HomePage(TemplateView):
    """
    View to render homepage.
    """
    template_name = "index.html"


@login_required
def make_booking(request):
    """
    View to render the create a booking page.
    """
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
    """
    View to render the view all bookings page.
    """
    bookings = request.user.bookings.all()
    context = {
        'bookings': bookings,
    }
    return render(request, 'my_account.html', context)


@login_required
def edit_booking(request, booking_id):
    """
    View to render to view to edit a booking
    """
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
    """
    View to render the page to delete a booking.
    """
    item = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Booking delete successful..')
        return redirect('my_account')
    context = {
        "booking": item
    }
    return render(request, "delete_items.html", context)


@login_required
def make_review(request):
    """
    Displays the review form if user is authorised.
    """
    if request.method == 'POST':
        review = Review(user=request.user)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Review posted. Wait for approval.'
                )
            return redirect('home')

    else:
        form = ReviewForm()
        context = {
            'form': form,
            'posted': True
            }
    return render(request, 'make_review.html', context)


def show_review(request):
    """
    Displays the reviews.
    """
    reviews = Review.objects.all().order_by('-creation_date')
    context = {
        'reviews': reviews,
    }
    return render(request, 'show_review.html', context)


def contact(request):
    """
    Displays the contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            html = render_to_string('emails/contactform.html', {
                'name': name,
                'email': email,
                'content': content
            })
            send_mail('The contact form subject ', 'This is the \
                message', 'noreply@gmail.com', ['andrewkennedy35@yahoo.ie'], html_message=html)
            messages.success(request, 'Message sent..')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {
        'form': form
        })
