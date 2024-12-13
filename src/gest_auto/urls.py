from django.urls import path
from .views import gestion_auto


urlpatterns = [
    path('', gestion_auto, name='gest_auto_view')
]