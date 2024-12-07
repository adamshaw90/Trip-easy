from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Itinerary, Booking
from .forms import SignUpForm, ProfileForm, ItineraryForm, BookingForm

def home(request):
    itineraries = Itinerary.objects.all()
    return render(request, 'booking/home.html', {'itineraries': itineraries})

def about(request):
    return render(request, 'booking/about.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful.")
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'booking/sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'booking/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'booking/profile.html')

@login_required
def profile_update(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'booking/profile_edit.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, "Account deleted.")
        return redirect('home')
    return render(request, 'booking/profile_delete_confirm.html')

# Itinerary CRUD
@login_required
def itinerary_create(request):
    if not request.user.is_superuser:
        messages.error(request, "Only admin can create itineraries.")
        return redirect('home')
    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Itinerary created.")
            return redirect('home')
    else:
        form = ItineraryForm()
    return render(request, 'booking/itinerary_form.html', {'form': form})

def itinerary_list(request):
    itineraries = Itinerary.objects.all()
    return render(request, 'booking/itinerary_list.html', {'itineraries': itineraries})

def itinerary_detail(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    return render(request, 'booking/itinerary_detail.html', {'itinerary': itinerary})

@login_required
def itinerary_update(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "Only admin can update itineraries.")
        return redirect('home')
    itinerary = get_object_or_404(Itinerary, pk=pk)
    if request.method == 'POST':
        form = ItineraryForm(request.POST, instance=itinerary)
        if form.is_valid():
            form.save()
            messages.success(request, "Itinerary updated.")
            return redirect('itinerary_detail', pk=pk)
    else:
        form = ItineraryForm(instance=itinerary)
    return render(request, 'booking/itinerary_form.html', {'form': form})

@login_required
def itinerary_delete(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "Only admin can delete itineraries.")
        return redirect('home')
    itinerary = get_object_or_404(Itinerary, pk=pk)
    if request.method == 'POST':
        itinerary.delete()
        messages.success(request, "Itinerary deleted.")
        return redirect('home')
    return render(request, 'booking/itinerary_confirm_delete.html', {'itinerary': itinerary})

# Booking a trip (User must be logged in and have a profile)
@login_required
def book_itinerary(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.itinerary = itinerary
            booking.save()
            messages.success(request, "Trip booked successfully!")
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form, 'itinerary': itinerary})
