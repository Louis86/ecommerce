from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest

# Create your views here.
def register(request):
    if request.method == "POST":
        fname = request.POST["first-name"]
        lname = request.POST["last-name"]
        email = request.POST["email"]
        country_code = request.POST["country-code"]
        phone = request.POST["phone-number"]
        password = request.POST["password"]
        role = request.POST["role"]

        address = request.POST["address"]
        address2 = request.POST.get("address2")
        city = request.POST["city"]
        state = request.POST["state"]
        country = request.POST["country"]
        zip = request.POST["zip"]


        User.objects.create_user(username=lname, email=email, first_name=fname, last_name=lname, password=password).save()
        #u = User.objects.get(username=email)

        return HttpResponse("logged in successfully")


    else:
        return render(request, "authentification/register.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)

            return HttpResponse("logged in successful")

        else:
            return HttpResponse("You entered wrong credentials.")

    else:
        """

         """
        return render(request, "authentification/login.html")


def logout_view(request):
    logout(request)
    return HttpResponse("logged out successfully")
