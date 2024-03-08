from django.db import models
from account.models import CustomUser, Department
    
class Requisition(models.Model):
    # Existing fields
    requester = models.ForeignKey(CustomUser, related_name='requested_requisitions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    amount_in_words = models.CharField(max_length=255)
    reason = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    approver = models.ForeignKey(CustomUser, related_name='approved_requisitions', on_delete=models.CASCADE, null=True, blank=True)
    charge_to_account = models.CharField(max_length=100, null=True, blank=True)
    account_name = models.CharField(max_length=100, null=True, blank=True)
    forwarded_to_cashier_by = models.ForeignKey(CustomUser, related_name='forwarded_requisitions', on_delete=models.CASCADE, null=True, blank=True)
    received_by = models.CharField(max_length=100, null=True, blank=True)
    date_received = models.DateTimeField(null=True, blank=True)
    cashier_signature = models.ImageField(upload_to='cashier_signatures/', null=True, blank=True)
    receiver_signature = models.ImageField(upload_to='receiver_signatures/', null=True, blank=True)
    voucher_number = models.CharField(max_length=100, null=True, blank=True)
    supervisor = models.ForeignKey(CustomUser, related_name='supervised_requisitions', on_delete=models.CASCADE)
    supervisor_comment = models.TextField(blank=True)
    supervisor_approval_date = models.DateTimeField(null=True, blank=True)
    phase = models.IntegerField(default=1)  
    STATUS_CHOICES = [
        ('Pending Supervisor Approval', 'Pending Supervisor Approval'),
        ('Pending Approver Approval', 'Pending Approver Approval'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Cash Out', 'Cash Out'),
    ]
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending Supervisor Approval')
    
    @property
    def requester_signature(self):
        return f"{self.requester.first_name.lower()}_{self.requester.last_name.lower()}.png"

    @property
    def supervisor_signature(self):
        if self.supervisor:
            return f"{self.supervisor.first_name.lower()}_{self.supervisor.last_name.lower()}.png"
        return ""

    @property
    def approver_signature(self):
        if self.approver:
            return f"{self.approver.first_name.lower()}_{self.approver.last_name.lower()}.png"
        return ""

    @property
    def cashier_signature_filename(self):
        return f"{self.cashier_signature.name.split('/')[-1]}"

    @property
    def receiver_signature_filename(self):
        return f"{self.receiver_signature.name.split('/')[-1]}"

    def __str__(self):
        return f"Requisition #{self.pk}"

