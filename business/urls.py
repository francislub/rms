from django.urls import path
from . import views


urlpatterns = [
    #path('', views.dashboard, name="adminDashboard"),
    path('requisition/', views.requisition_view, name="requisition"),
  
]