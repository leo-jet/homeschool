from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate, 
    get_user_model,
    login,
    logout,
    )
from accounts.forms import UserLoginForm

# Create your views here.
def login_view(request):
    form = UserLoginForm(request.POST or None, auto_id=False)
    if request.method == "POST":
        username = request.POST.get("username", -1)
        password = request.POST.get("password", -1)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("accueil")
        print request.user.is_authenticated()
        
    return render(request, "login.html", {"form":form})

def register_view(request):
    return render(request, "login.html", {})

def logout_view(request):
    logout(request)
    return redirect("login")