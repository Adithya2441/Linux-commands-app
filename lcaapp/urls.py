from django.urls import path,include
from lcaapp import views

urlpatterns = [
    path('',views.home,name='home'),
]