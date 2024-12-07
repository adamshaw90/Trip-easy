from django.contrib import admin
from .models import Itinerary, Booking, Review, Profile

admin.site.register(Itinerary)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Profile)