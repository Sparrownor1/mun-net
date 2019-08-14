from . import views
from django.urls import path

app_name = 'chair'

urlpatterns = [
    path('', views.index, name='index'),
    path('sheet/', views.sheet, name='sheet'),
    path('requests/', views.requests, name='requests'),
    path('requests/add/', views.add_request, name='add_request'),
    path('requests/delete/<request_key>', views.delete_request, name='delete_request'),
    path('requests/edit/<request_key>', views.edit_request, name='edit_request'),
]
