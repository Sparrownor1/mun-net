from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('', views.index, name='index'),
    path('login/', views.login_request, name="login"),
    path('account/', views.account, name="account"),
    
    path('password/', auth_views.PasswordChangeView.as_view()),
    path('password/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]
