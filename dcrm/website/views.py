from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .models import Author, Customer, Order


def home(request):
    orders = Order.objects.all()
    authors = Author.objects.all()
    customers = Customer.objects.all()

    # Check to see if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In")
            return redirect("home")
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again")
            return redirect("home")
    else:
        return render(request, "home.html", {"orders": orders})


def login_user(request):
    return redirect("home")


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect("home")


def customer_order(request, pk):
    if request.user.is_authenticated:
        customer_order = Order.objects.get(id=pk)
        return render(request, "order.html", {"customer_order": customer_order})
    else:
        messages.success(request, "You Must Be Logged In To View This Page")
        return redirect("home")
