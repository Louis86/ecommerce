from django.urls import path
from . import views
#add parmelink
urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.index, {'pagename':''}, name='home'),
    #path('<str:pagename>', views.index, name='index')
]
