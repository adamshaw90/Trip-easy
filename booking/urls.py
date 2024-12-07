from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/delete/', views.delete_profile, name='profile_delete'),
    path('itineraries/', views.itinerary_list, name='itinerary_list'),
    path('itineraries/create/', views.itinerary_create, name='itinerary_create'),
    path('itineraries/<int:pk>/', views.itinerary_detail, name='itinerary_detail'),
    path('itineraries/<int:pk>/update/', views.itinerary_update, name='itinerary_update'),
    path('itineraries/<int:pk>/delete/', views.itinerary_delete, name='itinerary_delete'),
    path('itineraries/<int:pk>/book/', views.book_itinerary, name='book_itinerary'),
]
