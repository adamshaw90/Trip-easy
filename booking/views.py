from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Itinerary, Booking, Profile
from .forms import BookingForm, ProfileForm
from django.contrib import messages

# View for booking an itinerary
@login_required
def book_itinerary(request, pk):
    if not hasattr(request.user, 'profile'):
        messages.error(request, 'You must complete your profile before booking an itinerary.')
        return redirect('complete_profile')  # Redirect to the profile completion page

    itinerary = get_object_or_404(Itinerary, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.itinerary = itinerary
            booking.save()
            messages.success(request, 'Your booking has been confirmed!')
            return redirect('booking_success')  # Redirect to a booking success page
    else:
        form = BookingForm()

    return render(request, 'booking/book_itinerary.html', {'itinerary': itinerary, 'form': form})

# View for completing the profile
@login_required
def complete_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your profile has been completed!')
            return redirect('home')  # Redirect to the homepage or dashboard
    else:
        form = ProfileForm()

    return render(request, 'booking/complete_profile.html', {'form': form})

# View for updating the profile
@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('home')  # Redirect to the homepage or dashboard
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'booking/update_profile.html', {'form': form})
