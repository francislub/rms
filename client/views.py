from django.shortcuts import render, redirect
from .forms import RequisitionPhase1Form, RequisitionPhase2Form, RequisitionPhase3Form

# Create your views here.

def login(request):
    return render(request, 'auth/login.html')

def register(request):
    return render(request, 'auth/reg.html')

def lock(request):
    return render(request, 'auth/lock_screen.html')

def dep(request):
    return render(request, 'dep.html')

def req(request):
    return render(request, 'client/req.html')


#===========Francis calling the dashbourd==============
def dashboard(request):
    return render(request, 'dashboard.html')
def client(request):
    return render(request, 'client.html')


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
