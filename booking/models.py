from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_ckeditor_5.fields import CKEditor5Field

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

class Itinerary(models.Model):
    name = models.CharField(max_length=200)
    description = CKEditor5Field('Description', config_name='default')
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='itineraries/', blank=True, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.itinerary.name}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.itinerary.name}"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        # Only save if the profile exists
        if hasattr(instance, 'profile'):
            instance.profile.save()