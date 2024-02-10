from django.contrib import admin
from django.urls import path,include
from .views import * 


urlpatterns = [
    path('getmerchant',GetMerchants.as_view()),
    path('getpin',GetPin.as_view()),    
]
