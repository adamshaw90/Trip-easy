from django.contrib import admin
from .models import UserProfile, Itinerary, Location, Booking, Review

admin.site.register(UserProfile)
admin.site.register(Itinerary)
admin.site.register(Location)
admin.site.register(Booking)
admin.site.register(Review)