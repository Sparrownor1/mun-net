from . import views
from django.urls import path, include

app_name = 'delegation'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_delegate/', views.add_delegate, name="add_delegate"),
    path("delete_delegate/<delegate_key>", views.delete_delegate, name="delete_delegate"),
    path("edit_delegate/<delegate_key>", views.edit_delegate, name="edit_delegate"),
    path("edit_delegation/", views.edit_delegation, name="edit_delegation"),
    path("upload_position_paper/<delegate_key>", views.upload_position_paper, name='upload_position_paper')
]
