from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="depDashboard"),
    path('reqstatus/', views.dep_reqStatus, name="reqStatus"),
    # path('repst/', views.reportStatus, name="repst"),
]