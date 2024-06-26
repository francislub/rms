from django import forms
from .models import Requisition

class RequisitionPhase1Form(forms.ModelForm):
    request_date = forms.DateTimeField(label='Request Date', required=False)  # Add request date field
    
    class Meta:
        model = Requisition
        fields = ['amount', 'reason', 'department', 'requester', 'request_date']  # Include request date field

class RequisitionPhase2Form(forms.ModelForm):
    supervisor_date = forms.DateTimeField(label='Supervisor Approval Date', required=False)  # Add supervisor date field
    
    class Meta:
        model = Requisition
        fields = ['supervisor', 'supervisor_comment', 'supervisor_date']  # Include supervisor date field

class RequisitionPhase3Form(forms.ModelForm):
    approver_date = forms.DateTimeField(label='Approver Approval Date', required=False)  # Add approver date field
    
    class Meta:
        model = Requisition
        fields = ['approver', 'charge_to_account', 'approver_date']  # Include approver date field
