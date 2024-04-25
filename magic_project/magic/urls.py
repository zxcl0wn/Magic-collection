from django.urls import path
from .views import *

urlpatterns = [
    path('cards/<str:color>/', color_page, name='color_page'),
    path('', home, name='home'),
]