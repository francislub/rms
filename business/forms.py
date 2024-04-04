from django import forms
from .models import DepartmentApproval

class DepartmentApprovalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(DepartmentApprovalForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(DepartmentApprovalForm, self).save(commit=False)
        if self.request:
            instance.approved_by = self.request.user
        if commit:
            instance.save()
        return instance

    class Meta:
        model = DepartmentApproval
        fields = ['department', 'approval_status', 'comments']
