from django.urls import path
from . import views

urlpatterns = [
    # path('', views.dashboard, name="depDashboard"),
    path('reqstatus/', views.dep_reqStatus, name="reqStatus"),
    path('approve/<int:requisition_id>/', views.department_approval, name='department_approval'),
]