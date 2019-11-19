from . import views
from django.urls import path, include
from django.contrib import admin

app_name = 'tenants'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
