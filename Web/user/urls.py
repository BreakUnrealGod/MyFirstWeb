from django.urls import path, re_path
from user.views import *
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('register',user_register, name='register'),
    path('login',user_login, name='login'),
    # re_path(r'^login/$', auth_views.LoginView.as_view(), name='login')
    path('logout',user_logout, name='logout'),
    path('usercenter', user_center, name='usercenter'),
    path('updatepassword', update_password, name='updatepassword'),
    # path('usergame', user_game, name='usergame'),
    path('userbackground', user_background, name='userbackground'),
]
