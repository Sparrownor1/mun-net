from . import views
from django.urls import path, include

app_name = 'secretariat'

urlpatterns = [
        path('', views.index, name='index'),
        path('add_chair/', views.add_chair, name='add_chair'),
        path('progress/', views.progress, name='progress'),
        path('progress/<slug>/', views.progress_sheet, name='progress_sheet'),
]
