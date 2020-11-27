from django.http import HttpResponse
from django.shortcuts import render
from django.views import View



class HomeView(View):
    template_name = "ecomapp/home.html"

    def get(self, request):
        # <view logic>
        return render(request, self.template_name)


class AboutView(View):
    template_name = "ecomapp/about.html"

    def get(self, request):
        # <view logic>
        return render(request, self.template_name)



"""
class AboutView(TemplateView):
    template_name = "about.html"



def index(request):
    #return HttpResponse("Hello, world. You're at the ecomapp index.")
    return render(request, "ecomapp/home.html")


def AboutView(request):

    return render(request, "ecomapp/about.html")
"""
