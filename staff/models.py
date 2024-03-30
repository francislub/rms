from django.db import models
from client.models import Requisition  
from account.models import CustomUser 

class DepartmentApproval(models.Model):
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE)
    department = models.ForeignKey('account.Department', on_delete=models.CASCADE)
    approved_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    approver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='approver')
    approved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Approval for Requisition {self.requisition.id} in {self.department.name}"
