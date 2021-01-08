from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import ProductList, DetailProductView , AboutView , TemplateView, View

app_name = 'ecomapp'

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', views.DetailProductView.as_view(), name='detail'),
    path('index/', views.Index.as_view(), name='index'),
]
