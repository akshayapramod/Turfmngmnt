from django.shortcuts import render

# Create your views here.
def bill_generation(request):
    return render(request,'mngrtemplates/bill_generation.html')
def bookings_history(request):
    return render(request,'mngrtemplates/bookings_history.html')
def check_rates(request):
    return render(request,'mngrtemplates/check_rates.html')
def confirm_booking(request):
    return render(request,'mngrtemplates/confirm_booking.html')
def login(request):
    return render(request,'mngrtemplates/login.html')
def view_request(request):
    return render(request,'mngrtemplates/view_request.html')
