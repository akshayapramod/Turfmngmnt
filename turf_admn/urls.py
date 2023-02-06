from django.urls import path
from . import views
app_name = 'turf_admn'
urlpatterns = [
    path('add_manager',views.add_manager,name='add_manager'),
    path('add_price_list',views.add_manager,name='add_price_list'),
    path('manage_turf',views.add_manager,name='manage_turf'),
    path('view_booking',views.add_manager,name='view_booking'),
]