from django.urls import path
from . import views

urlpatterns = [
    # path('', views.dashboard, name="adminDashboard"),
    path('reqst/', views.dep_reqStatus, name="reqst"),
    # path('repst/', views.reportStatus, name="repst"),
]