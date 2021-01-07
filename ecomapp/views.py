from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product
from django.urls import reverse
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.views.generic import ListView, DetailView,View
from .models import Product

class DetailProductView(generic.DetailView):
    template_name = "detail.html"


    def get_queryset(self):

        return Product.objects.filter()



class ProductList(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = "products/product_list.html"
    context = {
            'products': queryset
            }


    def get(self, request):
        # <view logic>
        return render(request, self.template_name, self.context)



class HomeView(generic.ListView):
    template_name = "home.html"

    products = Product.objects.all()
    context = {
            'products': products
            }
    def get(self, request):
        # <view logic>
        return render(request, self.template_name, self.context)




class AboutView(View):
    template_name = "about.html"

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
