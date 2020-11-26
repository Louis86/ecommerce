from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"



def index(request):
    #return HttpResponse("Hello, world. You're at the ecomapp index.")
    return render(request, "ecomapp/home.html")


def AboutView(request):

    return render(request, "ecomapp/about.html")
