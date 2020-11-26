from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'ecomapp'

urlpatterns = [
    path('', views.index, name='index'),
    #path('ecomapp/about/', views.AboutView, name='about'),
    path('about/', TemplateView.as_view(template_name="about.html")),

]