from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            print(f"User {user} authenticated successfully.")
            return redirect("home") 
        else:
            print("Authentication failed. User is None.")

    return render(request, "login.html")


def homepage(request):
    return render(request, "home.html")
