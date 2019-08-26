from . import views
from django.urls import path

app_name = 'chair'

urlpatterns = [
    path('', views.index, name='index'),
    path('sheet/', views.sheet, name='sheet'),
    path('position_papers/', views.position_papers, name='position_papers'),
    path('position_papers/download/<paper_key>', views.download_paper, name='download_paper'),
    path('requests/', views.requests, name='requests'),
    path('requests/add/', views.add_request, name='add_request'),
    path('requests/delete/<request_key>', views.delete_request, name='delete_request'),
    path('requests/edit/<request_key>', views.edit_request, name='edit_request'),
]
