from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                 # Home page
    path('about/', views.about, name='about'),         # About page
    path('register/', views.register, name='register'),# Registration page
    path('book/<int:pk>/', views.book_itinerary, name='book_itinerary'),
    path('update/<int:pk>/', views.update_booking, name='update_booking'),
]
