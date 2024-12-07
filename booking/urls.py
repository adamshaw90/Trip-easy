from django.urls import path
from . import views

urlpatterns = [
    path('itinerary/book/<int:pk>/', views.book_itinerary, name='book_itinerary'),
    path('profile/complete/', views.complete_profile, name='complete_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
]