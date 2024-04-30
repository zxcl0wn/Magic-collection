from django.urls import path
from .views import *

urlpatterns = [
    path('cards/<str:color>/', color_page, name='color_page'),
    path('', home, name='home'),
    path('collection/', collection_page, name='collection_page'),
    path('api/add_to_collection/', add_card_to_collection, name="add_to_collection")
]