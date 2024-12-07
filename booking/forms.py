from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Itinerary, Booking

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'address', 'phone_number']

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ['name', 'description', 'start_date', 'end_date', 'price']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = []
        # No fields needed, just a button to confirm booking
