from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import DepartmentApproval
from .forms import DepartmentApprovalForm

@login_required
def approve_requisition(request, requisition_id):
    # Assuming you have a method to retrieve the requisition object based on the requisition_id
    requisition = get_requisition(requisition_id)

    # Get the current user
    current_user = request.user

    # Determine the department of the current user (customize this based on your user model)
    department = current_user.department  # Assuming the department is a field on the user model

    # Determine the approver based on the department (customize this logic based on your requirements)
    approver = get_approver_for_department(department)

    if request.method == 'POST':
        form = DepartmentApprovalForm(request.POST)
        if form.is_valid():
            department_approval = form.save(commit=False)
            department_approval.requisition = requisition
            department_approval.department = department
            department_approval.approved_by = current_user
            department_approval.approver = approver
            department_approval.save()
            return redirect('requisition_detail', requisition_id=requisition.id)
    else:
        form = DepartmentApprovalForm(initial={'approver': approver})  # Pre-populate the form with the determined approver

    context = {
        'form': form,
        'requisition': requisition,
    }
    return render(request, 'approve_requisition.html', context)
