from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect 
from django.views import View

from django.http import HttpResponseRedirect, HttpResponse
import sys
# from django.core.urlresolvers import reverse
# from django.contrin.auth.decorators import login_required

# Create your views here.
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:

#         return render(request, 'login.html')
    
# def home(request):
#     return render(request, 'dashboard.html')

class Login(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render (request,self.template_name)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                wrongUser = {"message": "Wrong username or password"}
            else:
                login(request, user)
            return redirect('home')
        else: 
            wrongUser = {"message": "Wrong username or password"}

        # return render(request, 'login.html', wrongUser)
        return render(request, 'login.html', wrongUser)
    
class Home(View):
    template_name = 'dashboard.html'
    def get(self, request):
        if request.user.is_superuser:
            return redirect('/admin')
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')

# def user_login(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('index'))
            
#             else:
#                 return HttpResponse("ACCOUNTS NOT ACTIVE")
            
#         else:
#             print("Someone tried to login and failed!")
#             print("Username: {} and password {}".format(username,password))
#             return HttpResponse("Invalid login details supplied!")
#     else:
#         return render(request,'login.html')
    
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('login'))