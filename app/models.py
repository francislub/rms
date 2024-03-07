from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Requisition(models.Model):
    requester = models.ForeignKey(User, related_name='requested_requisitions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    amount_in_words = models.CharField(max_length=255)
    reason = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(User, related_name='supervised_requisitions', on_delete=models.CASCADE)
    approver = models.ForeignKey(User, related_name='approved_requisitions', on_delete=models.CASCADE, null=True, blank=True)
    charge_to_account = models.CharField(max_length=100, null=True, blank=True)
    account_name = models.CharField(max_length=100, null=True, blank=True)
    forwarded_to_cashier_by = models.ForeignKey(User, related_name='forwarded_requisitions', on_delete=models.CASCADE, null=True, blank=True)
    received_by = models.CharField(max_length=100, null=True, blank=True)
    date_received = models.DateTimeField(null=True, blank=True)
    cashier_signature = models.CharField(max_length=100, null=True, blank=True)
    receiver_signature = models.CharField(max_length=100, null=True, blank=True)
    voucher_number = models.CharField(max_length=100, null=True, blank=True)
    supervisor_signature = models.ImageField(upload_to='supervisor_signatures/', null=True, blank=True)
    checker1_signature = models.ImageField(upload_to='checker1_signatures/', null=True, blank=True)
    checker2_signature = models.ImageField(upload_to='checker2_signatures/', null=True, blank=True)
