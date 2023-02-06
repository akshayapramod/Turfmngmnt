from django.shortcuts import render

# Create your views here.
def book_turf(request):
    return render(request,'usertemplates/book_turf.html')
def booking_history(request):
    return render(request,'usertemplates/booking_history.html')
def check_availability(request):
    return render(request,'usertemplates/check_availability.html')
def check_turf(request):
    return render(request,'usertemplates/check_turf.html')
def user_home(request):
    return render(request,'usertemplates/user_home.html')