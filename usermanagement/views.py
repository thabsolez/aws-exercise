from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Staff


# Create your views here.

def welcome(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('username')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print("incorrect credentials") 
            return redirect('welcome')   
    else:

        return render(request, 'welcome.html')    

def dashboard(request):
    staff = Staff.objects.all()
    num = staff.count()  # Count of all staff members
    malenumber = staff.filter(gender='male').count()  # Count of male staff members
    femalenumber = staff.filter(gender='female').count()  # Count of female staff members
    male = staff.filter(gender='male')  # Queryset of male staff members
    female = staff.filter(gender='female')  # Queryset of female staff members

    context = {
        's': staff,
        'number': num,
        'malenumber': malenumber,
        'femalenumber': femalenumber,
        'male': male,
        'female': female,
    }

    return render(request, 'dashboard.html', context)
      