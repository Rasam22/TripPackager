from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/add_city/', views.add_city, name='add_city'),
    path('',LoginView.as_view(),name='login'),
    path('register/',views.registerView,name='register'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
]