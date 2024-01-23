from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . views import Login, Home, Logout

urlpatterns = [
    
    path('', Login.as_view(), name='login'), # custom login view
    path('home/', Home.as_view(), name='home'),
    path('logout/', Logout.as_view(), name='logout'), # Django's built-in logout view

]

