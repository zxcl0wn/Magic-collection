from django.urls import path
from .views import *

urlpatterns = [
    path('<str:color>/', color_page, name='color_page'),
    # path('multi_color_page/', multi_color_page, name='multi_color_page'),

]