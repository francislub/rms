from django.shortcuts import render, redirect
from django.contrib import messages
from staff.models import DepartmentApproval
from client.models import Requisition  
# from account.models import CustomUser  

def business_approval(request, requisition_id):
    requisition = Requisition.objects.get(id=requisition_id)
    department = requisition.department
    current_user = request.user  

    if current_user.user_type != 3:  # Assuming user_type 3 is for business approvals
        messages.error(request, "You are not authorized to approve requisitions at this level.")
        return redirect('some_redirect_view')  

    requisition_approvals = DepartmentApproval.objects.filter(requisition=requisition)

    if request.method == 'POST':
        form = DepartmentApproval(request.POST)
        if form.is_valid():
            department_approval = form.save(commit=False)
            department_approval.requisition = requisition
            department_approval.department = department
            department_approval.approved_by = current_user
            department_approval.save()

            if department_approval.approval_status == 'APPROVED':
                requisition.status = 'APPROVED'
            else:
                requisition.status = 'REJECTED'
            requisition.save()

            messages.success(request, "Requisition has been approved successfully.")
            return redirect('some_redirect_view')  
    else:
        form = DepartmentApproval()

    context = {
        'form': form,
        'requisition': requisition,
        'requisition_approvals': requisition_approvals,
    }
    return render(request, 'business_approval.html', context)

def dep_reqStatus(request):
    requisitions = Requisition.objects.all()
    return render(request, "depReqStatus.html", {'requisitions': requisitions})




