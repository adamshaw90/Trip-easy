from django.contrib import admin
from .models import Profile, Itinerary, Booking, Review, ContactRequest

admin.site.register(Profile)
admin.site.register(Itinerary)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(ContactRequest)
