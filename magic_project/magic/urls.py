from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('white_page/', white_page, name='white_page'),

]