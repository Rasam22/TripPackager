from django.shortcuts import render, redirect
import requests
from .models import WH
from .models import seasons
from .models import fixedItems
from .models import seasonalItems
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'weather/index.html')

# To register user
def user_registration(request):
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        # If the request params is valid save the data else return form with error
    return render(request, 'registration/registration.html', {'form': form})

# To login user after authentication
def user_profile(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:        
            return redirect('home/')
        else :
            msg = "Enter Correct Details"
            return render(request,'registration/login.html',{'message':msg})
    else:
        return render(request,'registration/login.html')

# To display list of items according to users needs

@csrf_exempt
def add_city(request):
    current_date = timezone.now()
    city = request.POST.get('content')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c812a2a33fd7892739ba5b4c09b2e499'

    result = requests.get(url.format(city))
    if(result.status_code!=200):
        err = "This place doesnot exist. Please enter correct Name"
        messages.error(request, err)
        return redirect('/home/')
    
    r = result.json()
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
