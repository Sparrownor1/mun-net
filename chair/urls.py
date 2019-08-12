from . import views
from django.urls import path

app_name = 'chair'

urlpatterns = [
    path('', views.index, name='index'),
]
