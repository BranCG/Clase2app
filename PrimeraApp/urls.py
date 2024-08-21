
from django.urls import path
from PrimeraApp import views 

urlpatterns = [
    path("ahora/", views.displayDateTime)
]
