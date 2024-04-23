from django.urls import path
from .views import *

urlpatterns = [
    path('<str:color>/', color_page, name='color_page'),

]