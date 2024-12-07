from django.db import models
from django.contrib.auth.models import User

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username
       
# Itinerary model
class Itinerary(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

# Booking model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} booking for {self.itinerary.name}'

# Review model
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.itinerary.name} review by {self.user.username}'