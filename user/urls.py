from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    path('book_turf',views.book_turf,name='book_turf'),
    path('booking_history',views.booking_history,name='booking_history'),
    path('check_availability',views.check_availability,name='check_availability'),
    path('check_turf',views.check_turf,name='check_turf'),
]