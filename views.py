from django.shortcuts import render, redirect
from django.contrib import messages
from nameApp.models import Reservation

# Create your views here.
def home(request):
    res = Reservation.objects.all()
    return render(request, 'index.html', {"reservation": res} )


def create_res(request):
    Reservation.objects.create(
    #if request.method == "POST":
        first_name=request.POST.get("first_name"),
        last_name=request.POST.get("last_name"),
        email=request.POST.get("email"),
        location=request.POST.get("location"),
        date=request.POST.get("date"),
        time=request.POST.get("time")
    )
    messages.success(request, "Reservation Created Successfully!")
    return redirect('/home/')