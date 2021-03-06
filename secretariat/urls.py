from . import views
from django.urls import path, include

app_name = 'secretariat'

urlpatterns = [
        path('', views.index, name='index'),
        path('add_chair/', views.add_chair, name='add_chair'),
        path('progress/', views.progress, name='progress'),
        path('progress/<slug>/', views.progress_sheet, name='progress_sheet'),
        path('requests/', views.requests, name='requests'),
        path('requests/change_status/<request_key>/', views.change_status, name='change_status'),
        path('allocations/', views.allocations, name='allocations'),
        path('allocations/add_del/', views.add_allocation_delegate, name='add_allocation_delegate'),
        path('allocations/delete_del/', views.delete_allocation_delegate, name='delete_allocation_delegate'),
]
