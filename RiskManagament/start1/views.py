from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .forms import InherentRiskForm, IntegralActivityForm, MajorActivityForm, ObjectiveForm, RmcdUserForm, IadUserForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 
from .models import WorkUnit, MajorActivity, IntegralActivity, Objective,InherentRisk
from django.forms import inlineformset_factory
from django import forms
from .calculation import cal


@login_required(login_url='login')
def homepage(request):
    registerRisk = InherentRisk.objects.filter(added_by=request.user)
        
    offices = WorkUnit.objects.filter(type="Office")
    departments = WorkUnit.objects.filter(type="Department")
    branches = WorkUnit.objects.filter(type="Branch")
    TotalScore = cal.totalScore(registerRisk)
    RiskGrade = cal.grade(TotalScore)
   
    if request.method=='POST':
        selected_item = get_object_or_404(WorkUnit, pk=request.POST.get('item_id'))
        risk = WorkUnit.objects.filter(code=selected_item.code)
        IR = InherentRisk.objects.filter(User).filter(WorkUnit).filter(name = risk.name)
        context1 = {'inherentRisk':IR}
        return render(request, 'rmcdUser.html', context1)

    context = {'registerRisk':registerRisk, 'offices':offices, 'departments':departments, 'branches':branches, 'TotalScore':TotalScore, 'RiskGrade':RiskGrade}
    return render(request, 'homepage.html', context)

def viewDetail(request):
    context = {}
    return render(request, 'viewDetail.html', context)

def register(request):
    if request.method == 'POST':
        f = UserRegisterForm(request.POST)
        if f.is_valid():
            form = f.save(commit=False)
            form.is_active = False
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

    else:
        f = UserRegisterForm()

    return render(request, 'register.html', {'form': f})

def loginpage(request):
    
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, 'Username OR Password is incorrect')
                

        return render(request, 'login.html', {})

def logoutpage(request):
    logout(request)
    return redirect('login')

#MAJOR ACTIVITY
def majorActivity(request):
    MA = MajorActivity.objects.filter(added_by=request.user)
  
    form = MajorActivityForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.added_by = request.user
        form.save()
        messages.success(request, 'Saved successfully')
        return redirect('integralActivity')
  
    context ={'majorActivity':MA, 'form':form}
    return render(request, "majorActivity.html", context)

# update major activity
def updateMajorActivity(request, pk):
    MA = MajorActivity.objects.filter(added_by=request.user)
    ma = MajorActivity.objects.get(id=pk)
    form = MajorActivityForm(instance=ma)

    if request.method == 'POST':
        form = MajorActivityForm(request.POST, instance=ma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('majorActivity')

    context = {'form': form, 'majorActivity':MA}
    return render(request, 'updateMajorActivity.html', context)

# delete major activity
def deleteMajorActivity(request, pk):
    ma = MajorActivity.objects.get(id=pk)
    if request.method == 'POST':
        ma.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('majorActivity')
    
    context = {'item':ma}
    return render(request, 'deleteMajorActivity.html', context)


#INTEGRAL ACTIVITY
def integralActivity(request):
    IA = IntegralActivity.objects.filter(added_by=request.user)
    form = IntegralActivityForm(request.user or None, request.POST or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.added_by = request.user
        form.save()
        messages.success(request, 'Saved successfully')
        return redirect('objective')
  
    context ={'integralActivity':IA, 'form':form}
    return render(request, "integralActivity.html", context)

#CREATE INTEGRAL ACTIVITY
def createIntegralActivity(request, pk):
    ma = MajorActivity.objects.get(id=pk)
    form = IntegralActivityForm(instance=ma)

    if request.method == 'POST':
        form = IntegralActivityForm(request.POST, instance=ma)
        if form.is_valid():
            form = form.save(commit=False)
            form.added_by = request.user
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('majorActivity')

    context = {'form': form, 'majorActivity':ma}
    return render(request, "createIntegralActivity.html", context)

#uUPDATE INTEGRAL ACTIVITY
def updateIntegralActivity(request, pk):
    IA = IntegralActivity.objects.filter(added_by=request.user)
    ma = IntegralActivity.objects.get(id=pk)
    form = IntegralActivityForm(request.user or None, instance=ma)

    if request.method == 'POST':
        form = IntegralActivityForm(request.user or None, request.POST or None, instance=ma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('integralActivity')

    context = {'form': form, 'integralActivity':IA}
    return render(request, "updateIntegralActivity.html", context)

#delete INTEGRAL ACTIVITY
def deleteIntegralActivity(request, pk):
    ma = IntegralActivity.objects.get(id=pk)
    if request.method == 'POST':
        ma.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('integralActivity')
    
    context = {'item':ma}
    return render(request, "deleteIntegralActivity.html", context)

#OBJECTIVE
def objective(request):
    O = Objective.objects.filter(added_by=request.user)
    form = ObjectiveForm(request.user or None, request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.added_by = request.user
        form.save()
        messages.success(request, 'Saved successfully')
        return redirect('inherentRisk')
  
    context ={'objective':O, 'form':form}
    return render(request, "objective.html", context)

#CREATE OBJECTIVE
def createObjective(request, pk):
    IFormSet = inlineformset_factory(IntegralActivity, Objective, fields=('integral_Activity', 'name', 'added_by'), widgets = {'added_by': forms.HiddenInput()}, extra=1)
    
    ma = IntegralActivity.objects.get(id=pk) 
    # create object of form
    form = IFormSet(queryset=Objective.objects.none(), instance=ma)
    if request.method == 'POST':
        form = IFormSet(request.POST, instance=ma)
    # check if form data is valid
        if form.is_valid():
            form = form.save(commit=False)
            form.added_by = request.user
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('integralActivity')
    
    context ={'integralActivity':ma, 'form':form}
    return render(request, "createObjective.html", context)

#UPDATE OBJECTIVE
def updateObjective(request, pk):
    IA = Objective.objects.filter(added_by=request.user)
    ma = Objective.objects.get(id=pk)
    form = ObjectiveForm(request.user or None, instance=ma)

    if request.method == 'POST':
        form = ObjectiveForm(request.user or None, request.POST, instance=ma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('objective')

    context = {'form': form, 'objective':IA}
    return render(request, "updateObjective.html", context)


#DELETE OBJECTIVE
def deleteObjective(request, pk):
    ma = Objective.objects.get(id=pk)
    if request.method == 'POST':
        ma.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('objective')
    
    context = {'item':ma}
    return render(request, "deleteObjective.html", context)

#INHERENT RISK
def inherentRisk(request):
    IR = InherentRisk.objects.filter(added_by=request.user)
    form = InherentRiskForm(request.user or None, request.POST or None, request.FILES or None)
      
    if form.is_valid():
        form = form.save(commit=False)
        form.added_by = request.user
        monetaryValue = cal.monetaryValue(form.monetary_Value)
        consequence = cal.consequence(form.risk_Condition, monetaryValue)
        controlLayer = cal.controlLayer(form.it_System, form.privilage, form.procedure_Manual, form.maker_Checker, form.dual_Control)
        likelihood = cal.likelihood(controlLayer, form.frequency_of_Exposure)
        level = cal.riskLevel(consequence, likelihood)
        form.level = level
        form.save()
        messages.success(request, 'Saved successfully')
        return redirect('inherentRisk')
  
    context ={'inherentRisk':IR, 'form':form}
    return render(request, "inherentRisk.html", context)

#CREATE RISK
def createRisk(request, pk):
    IFormSet = inlineformset_factory(Objective, InherentRisk, fields=('objective', 'name'), extra=1)
    
    ma = Objective.objects.get(id=pk) 
    # create object of form
    form = IFormSet(queryset=InherentRisk.objects.none(), instance=ma)
    if request.method == 'POST':
        form = IFormSet(request.POST, instance=ma)
    # check if form data is valid
        if form.is_valid():
            form = form.save(commit=False)
            form.added_by = request.user
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('objective')
    
    context ={'objective':ma, 'form':form}
    return render(request, "createRisk.html", context)

    
#UPDATE INHERENTRISK
def updateInherentRisk(request, pk):
    IR = InherentRisk.objects.filter(added_by=request.user)
    ma = InherentRisk.objects.get(id=pk)
    form = InherentRiskForm(request.user or None, instance=ma)

    if request.method == 'POST':
        form = InherentRiskForm(request.user or None, request.POST, instance=ma)
        if form.is_valid():
            form = form.save(commit=False)
            monetaryValue = cal.monetaryValue(form.monetary_Value)
            consequence = cal.consequence(form.risk_Condition, monetaryValue)
            controlLayer = cal.controlLayer(form.it_System, form.privilage, form.procedure_Manual, form.maker_Checker, form.dual_Control)
            likelihood = cal.likelihood(controlLayer, form.frequency_of_Exposure)
            level = cal.riskLevel(consequence, likelihood)
            form.level = level
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('inherentRisk')

    context = {'form': form, 'inherentRisk':IR}
    return render(request, "updateInherentRisk.html", context)


#DELETE INHERENT RISK
def deleteInherentRisk(request, pk):
    ma = InherentRisk.objects.get(id=pk)
    if request.method == 'POST':
        ma.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('inherentRisk')
    
    context = {'item':ma}
    return render(request, "deleteInherentRisk.html", context)

def rmcdUser(request):
    IR = InherentRisk.objects.all()
    context = {'inherentRisk':IR}
    return render(request, 'rmcdUser.html', context)

def updateRmcdUser(request, pk):
    IR = InherentRisk.objects.all()
    ma = InherentRisk.objects.get(id=pk)
    form = RmcdUserForm(instance=ma)

    if request.method == 'POST':
        form = RmcdUserForm(request.POST, instance=ma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('rmcdUser')

    context = {'form': form, 'rmcdUser':IR}
    return render(request, "updateRmcdUser.html", context)

def iadUser(request):
    IR = InherentRisk.objects.all()
    form = IadUserForm()
    context = {'inherentRisk':IR, 'form':form}
    return render(request, 'iadUser.html', context)


def updateIadUser(request, pk):
    IR = InherentRisk.objects.all()
    ma = InherentRisk.objects.get(id=pk)
    form = IadUserForm(instance=ma)

    if request.method == 'POST':
        form = IadUserForm(request.POST, instance=ma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('iadUser')

    context = {'form': form, 'iadUser':IR}
    return render(request, "updateIadUser.html", context)
