from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('lock/', views.lock, name='register'),
    path('dep/', views.dep, name='dep'),
    path('req/', views.req, name='req'),
    path('',views.dashboard,name='dashboard'),
]