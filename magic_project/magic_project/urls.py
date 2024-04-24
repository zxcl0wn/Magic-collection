from django.contrib import admin
from django.urls import path, include

from magic.views import *

urlpatterns = [
    path('', include('magic.urls'))
]

# handler404 = pageNotFound