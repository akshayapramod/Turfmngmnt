from django.urls import path
from . import views
app_name = 'manager'
urlpatterns = [
    path('bill_generation',views.bill_generation,name='bill_generation'),
    path('bookings_history',views.bookings_history,name='bookings_history'),
    path('check_rates',views.check_rates,name='check_rates'),
    path('confirm_booking',views.confirm_booking,name='confirm_booking'),
    path('login',views.login,name='login'),
    path('view_request',views.view_request,name='view_request'),
]