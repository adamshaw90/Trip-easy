from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    preferred_language = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username
       
class Itinerary(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.CharField(max_length=50)
    max_participants = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return self.name

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Pending', 'Pending'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.itinerary.name}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()  # Typically 1-5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.itinerary.name}"