from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Itinerary, Booking, Review


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = ['full_name', 'address', 'phone_number']

    def __init__(self, *args, **kwargs):
        # Get the user instance passed from the view
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Set initial value for the email field
        if self.user:
            self.fields['email'].initial = self.user.email

    def save(self, commit=True):
        # Save the profile fields
        profile = super().save(commit=False)
        # Update the user's email
        if self.user:
            self.user.email = self.cleaned_data['email']
            if commit:
                self.user.save()
        if commit:
            profile.save()
        return profile


class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ['name', 'description', 'start_date', 'end_date', 'price']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = []


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'review_text': forms.
            Textarea(attrs={'placeholder': 'Write your review here...'}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
