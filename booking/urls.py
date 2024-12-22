from django.urls import path
from . import views
from .views import itinerary_detail, edit_review, delete_review, confirm_logout_view, confirm_cancel_booking

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
   path('logout/', confirm_logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/delete/', views.delete_profile, name='profile_delete'),
    path('itineraries/', views.itinerary_list, name='itinerary_list'),
    path('itineraries/', views.itineraries, name='itineraries'),
    path('itineraries/create/', views.itinerary_create, name='itinerary_create'),
    path('itineraries/<int:pk>/', views.itinerary_detail, name='itinerary_detail'),
    path('itineraries/<int:pk>/update/', views.itinerary_update, name='itinerary_update'),
    path('itineraries/<int:pk>/delete/', views.itinerary_delete, name='itinerary_delete'),
    path('itineraries/<int:pk>/book/', views.book_itinerary, name='book_itinerary'),
    path('review/<int:review_id>/edit/', edit_review, name='edit_review'),
    path('review/<int:review_id>/delete/', delete_review, name='delete_review'),
    path('booking/<int:booking_id>/cancel/', confirm_cancel_booking, name='cancel_booking'),

]
