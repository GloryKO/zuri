from django.urls import path 
from . import views
app_name= 'mycv'
urlpatterns = [
    path('',views.contact,name='contact'),
]