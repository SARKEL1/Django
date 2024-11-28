from django.contrib import admin
from django.urls import path, include
from website.views import welcome,date,otobie,detail,rooms_list
from . import views
urlpatterns = [
   path('<int:id>',detail,name='detail'),
    path('rooms',rooms_list,name='rooms'),
    path('new', views.new, name='new'),
]