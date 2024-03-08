# forms.py

from django import forms
from .models import Requisition

class RequisitionPhase1Form(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = ['amount', 'reason', 'department', 'requester_name', 'requester_signature']

class RequisitionPhase2Form(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = ['supervisor_name', 'supervisor_signature', 'supervisor_comment']

class RequisitionPhase3Form(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = ['approver_name', 'approver_signature', 'charge_to_account']

# views.py

from django.shortcuts import render, redirect
from .forms import RequisitionPhase1Form, RequisitionPhase2Form, RequisitionPhase3Form
from .models import Requisition

def requisition_phase1(request):
    if request.method == 'POST':
        form = RequisitionPhase1Form(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.phase = 1
            requisition.save()
            return redirect('requisition_phase2')
    else:
        form = RequisitionPhase1Form()
    return render(request, 'requisition_phase1.html', {'form': form})

def requisition_phase2(request):
    if request.method == 'POST':
        form = RequisitionPhase2Form(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.phase = 1
            requisition.save()
            return redirect('requisition_phase2')
    else:
        form = RequisitionPhase2Form()
    return render(request, 'requisition_phase2.html', {'form': form})

def requisition_phase3(request):
    if request.method == 'POST':
        form = RequisitionPhase3Form(request.POST)
        if form.is_valid():
            requisition = form.save(commit=False)
            requisition.phase = 1
            requisition.save()
            return redirect('requisition_phase3')
    else:
        form = RequisitionPhase2Form()
    return render(request, 'requisition_phase1.html', {'form': form})

# Similar views for other phases
