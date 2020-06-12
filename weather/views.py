from django.shortcuts import render, redirect
import requests
from .models import WH
from .models import seasons
from .models import fixedItems
from .models import seasonalItems
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'weather/index.html')

def registerView(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

@csrf_exempt
def add_city(request):
    current_date = timezone.now()
    city = request.POST["content"]
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c812a2a33fd7892739ba5b4c09b2e499'

    r = requests.get(url.format(city)).json()
    city_weather= {'city': city,
            'temperature': r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
                  }
    temp=city_weather['temperature']
    Seasons = seasons.objects.all()
    matchedSeasons=[]
    for s in Seasons:
        if float(s.temperatureStart)<=temp and float(s.temperatureEnd)>=temp:
            matchedSeasons.append(s.season)

    ItemsToCarry = []
    fixed= fixedItems.objects.all()
    for i in fixed:
        ItemsToCarry.append(i.items)
    variableItems = seasonalItems.objects.all()
    for i in variableItems:
        if i.season in matchedSeasons:
            ItemsToCarry.append(i.item)
    return render(request, 'weather/tripList.html', {'city': city_weather['city'],'temp':city_weather['temperature'],'desc':city_weather['description'],'icon':city_weather['icon'],'items':ItemsToCarry})
