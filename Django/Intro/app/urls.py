from django.urls import path
from .views import *
urlpatterns = [
    path('', LPU, name="land"),
    path('about/', about, name="about"),
    path('save/', save_data, name='save_data'),
]
