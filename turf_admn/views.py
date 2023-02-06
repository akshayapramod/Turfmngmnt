from django.shortcuts import render

# Create your views here.
def add_manager(request):
    return render(request,'admntemplates/add_manager.html')
def add_price_list(request):
    return render(request,'admntemplates/add_price_list.html')
def manage_turf(request):
    return render(request,'admntemplates/manage_turf.html')
def view_booking(request):
    return render(request,'admntemplates/view_booking.html')
