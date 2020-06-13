from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import home,user_registration , user_profile

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/add_city/', views.add_city, name='add_city'),
    path('user-registration', user_registration, name='user_registration'),
    path('', user_profile, name='user_profile'),
    path('logout/',LogoutView.as_view(next_page='user_profile'),name='logout'),
]