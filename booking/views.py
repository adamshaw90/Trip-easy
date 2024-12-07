from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm, BookingForm, ReviewForm
from .models import Itinerary, Booking

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Booking View
def book_itinerary(request, itinerary_id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.itinerary = itinerary
            booking.save()
            messages.success(request, 'Booking successful!')
            return redirect('itinerary_detail', itinerary_id=itinerary.id)
    else:
        form = BookingForm()
    return render(request, 'book_itinerary.html', {'form': form, 'itinerary': itinerary})

# Review View
def leave_review(request, itinerary_id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.itinerary = itinerary
            review.save()
            messages.success(request, 'Thank you for your review!')
            return redirect('itinerary_detail', itinerary_id=itinerary.id)
    else:
        form = ReviewForm()
    return render(request, 'leave_review.html', {'form': form, 'itinerary': itinerary})
