from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('white_page/', white_page, name='white_page'),
    path('blue_page/', blue_page, name='blue_page'),
    path('black_page/', black_page, name='black_page'),
    path('red_page/', red_page, name='red_page'),
    path('green_page/', green_page, name='green_page'),
    path('colorless_page/', colorless_page, name='colorless_page'),
    path('multi_color_page/', multi_color_page, name='multi_color_page'),
]