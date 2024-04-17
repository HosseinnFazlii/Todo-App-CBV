from django.urls import path,include
from django.contrib.auth.views import LogoutView
from .views import RegisterPage,UserLogin
app_name = 'accounts' 
urlpatterns = [
    path('login/', UserLogin.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('register/',RegisterPage.as_view(),name='register')
   
]
