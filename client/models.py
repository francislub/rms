from django.db import models
from account.models import CustomUser, Department
    
class Requisition(models.Model):
    requester = models.ForeignKey(CustomUser, related_name='requested_requisitions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    amount_in_words = models.CharField(max_length=255)
    reason = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(CustomUser, related_name='supervised_requisitions', on_delete=models.CASCADE)
    approver = models.ForeignKey(CustomUser, related_name='approved_requisitions', on_delete=models.CASCADE, null=True, blank=True)
    charge_to_account = models.CharField(max_length=100, null=True, blank=True)
    account_name = models.CharField(max_length=100, null=True, blank=True)
    forwarded_to_cashier_by = models.ForeignKey(CustomUser, related_name='forwarded_requisitions', on_delete=models.CASCADE, null=True, blank=True)
    received_by = models.CharField(max_length=100, null=True, blank=True)
    date_received = models.DateTimeField(null=True, blank=True)
    cashier_signature = models.ImageField(upload_to='cashier_signatures/', null=True, blank=True)
    receiver_signature = models.ImageField(upload_to='receiver_signatures/', null=True, blank=True)
    voucher_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Requisition #{self.pk}"
