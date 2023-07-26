from django.urls import path
from . import views
urlpatterns = [

    path('',views.viewfun,name='viewfun'),
    path('add/',views.addition,name='addition'),


]