from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Itinerary, Booking, Review
from .forms import SignUpForm, ProfileForm, ItineraryForm, BookingForm, ReviewForm

def home(request):
    itineraries = Itinerary.objects.all()
    return render(request, 'booking/home.html', {'itineraries': itineraries})

def about(request):
    return render(request, 'booking/about.html')

def itineraries(request):
    itineraries = Itinerary.objects.all()  # Retrieve all itineraries
    return render(request, 'booking/itineraries.html', {'itineraries': itineraries})    

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

def confirm_logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('home')
    return render(request, 'booking/confirm_logout.html')    

@login_required
def profile_view(request):
    profile = request.user.profile
    
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/profile.html', {
        'profile': profile,
        'user_bookings': user_bookings
    })

@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Your booking has been canceled.")
        return redirect('profile')
    else:
        
        return redirect('profile')

@login_required
def confirm_cancel_booking(request, booking_id):
    """Ask the user to confirm before canceling their booking."""
    # Ensure only the owner (or admin) can cancel this booking
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    
    if request.method == 'POST':
        # User confirmed cancellation
        booking.delete()  # or set a 'canceled' flag if you prefer soft-deletion
        messages.success(request, "Booking canceled successfully.")
        return redirect('profile')  # or wherever you redirect after cancellation
    
    # For GET requests, show the confirmation template
    return render(request, 'booking/confirm_cancel_booking.html', {'booking': booking})


@login_required
def profile_update(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile, user=request.user)
    return render(request, 'booking/profile_edit.html', {'form': form})

    
@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, "Account deleted.")
        return redirect('home')
    return render(request, 'booking/profile_delete_confirm.html')


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

def itinerary_detail(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    reviews = Review.objects.filter(itinerary=itinerary).order_by('-created_at')

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.itinerary = itinerary
                review.save()
                messages.success(request, "Review submitted successfully.")
                return redirect('itinerary_detail', pk=pk)
        else:
            form = ReviewForm()
    else:
        form = None

    return render(request, 'booking/itinerary_detail.html', {
        'itinerary': itinerary,
        'reviews': reviews,
        'review_form': form
    })

@login_required
def edit_review(request, review_id):
    """Allow the review owner or admin to edit their review."""
    review = get_object_or_404(Review, id=review_id)

    # Authorization check: only the review’s owner or superuser can edit
    if request.user != review.user and not request.user.is_superuser:
        messages.error(request, "You do not have permission to edit this review.")
        return redirect('itinerary_detail', pk=review.itinerary.pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully.")
            return redirect('itinerary_detail', pk=review.itinerary.pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'booking/edit_review.html', {
        'form': form,
        'review': review
    })

@login_required
def delete_review(request, review_id):
    """Allow the review owner or admin to delete their review."""
    review = get_object_or_404(Review, id=review_id)

    # Authorization check
    if request.user != review.user and not request.user.is_superuser:
        messages.error(request, "You do not have permission to delete this review.")
        return redirect('itinerary_detail', pk=review.itinerary.pk)

    if request.method == 'POST':
        itinerary_id = review.itinerary.pk
        review.delete()
        messages.success(request, "Review deleted successfully.")
        return redirect('itinerary_detail', pk=itinerary_id)

    return render(request, 'booking/confirm_delete_review.html', {'review': review})    