from django.urls import path,include
from lcaapp import views

urlpatterns = [
    path('',views.Myview.as_view(),name='home'),
]