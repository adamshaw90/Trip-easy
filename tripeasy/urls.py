from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]
