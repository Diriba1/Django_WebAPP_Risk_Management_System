from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomUserCreationForm, InherentRiskForm, IntegralActivityForm, MajorActivityForm, ObjectiveForm, RmcdUserForm, IadUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 
from .models import Branch, MajorActivity, IntegralActivity, Objective,InherentRisk
from django.forms import inlineformset_factory


@login_required(login_url='login')
def homepage(request):
    IR = InherentRisk.objects.all()
    offices = Branch.objects.filter(type="Office")
    departments = Branch.objects.filter(type="Department")
    branches = Branch.objects.filter(type="Branch")

    if request.method=='POST':
        selected_item = get_object_or_404(Branch, pk=request.POST.get('item_id'))
        risk = Branch.objects.filter(code=selected_item.code)
        context1 = {'risk': risk}
        return render(request, 'viewDetail.html', context1)

    context = {'inherentRisk':IR, 'offices':offices, 'departments':departments, 'branches':branches}
    return render(request, 'homepage.html', context)

def viewDetail(request):
    context = {}
    return render(request, 'viewDetail.html', context)

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = CustomUserCreationForm()

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
                messages.error(request, 'Username OR password is incorrect')
                

        return render(request, 'login.html', {})

def logoutpage(request):
    logout(request)
    return redirect('login')

#MAJOR ACTIVITY
def majorActivity(request):
    MA = MajorActivity.objects.all()
  
    # create object of form
    form = MajorActivityForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        form.save()
        messages.success(request, 'Saved successfully')
        return redirect('majorActivity')
  
    context ={'majorActivity':MA, 'form':form}
    return render(request, "majorActivity.html", context)

# update major activity
def updateMajorActivity(request, pk):
    MA = MajorActivity.objects.all()
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
    IA = IntegralActivity.objects.all()
  
    # create object of form
    form = IntegralActivityForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        form.save()
        messages.success(request, 'Saved successfully')
        return redirect('integralActivity')
  
    context ={'integralActivity':IA, 'form':form}
    return render(request, "integralActivity.html", context)

#CREATE INTEGRAL ACTIVITY
def createIntegralActivity(request, pk):
    IFormSet = inlineformset_factory(MajorActivity, IntegralActivity, fields=('major_Activity', 'name'), extra=5)
    
    ma = MajorActivity.objects.get(id=pk) 
    # create object of form
    form = IFormSet(queryset=IntegralActivity.objects.none(), instance=ma)
    if request.method == 'POST':
        form = IFormSet(request.POST, instance=ma)
    # check if form data is valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('majorActivity')
    
    context ={'majorActivity':ma, 'form':form}
    return render(request, "createIntegralActivity.html", context)

#uUPDATE INTEGRAL ACTIVITY
def updateIntegralActivity(request, pk):
    IA = IntegralActivity.objects.all()
    ma = IntegralActivity.objects.get(id=pk)
    form = IntegralActivityForm(instance=ma)

    if request.method == 'POST':
        form = IntegralActivityForm(request.POST, instance=ma)
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
    O = Objective.objects.all()
    form = ObjectiveForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Saved successfully')
        return redirect('objective')
  
    context ={'objective':O, 'form':form}
    return render(request, "objective.html", context)

#CREATE OBJECTIVE
def createObjective(request, pk):
    IFormSet = inlineformset_factory(IntegralActivity, Objective, fields=('integral_Actitivty', 'name'), extra=5)
    
    ma = IntegralActivity.objects.get(id=pk) 
    # create object of form
    form = IFormSet(queryset=Objective.objects.none(), instance=ma)
    if request.method == 'POST':
        form = IFormSet(request.POST, instance=ma)
    # check if form data is valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('integralActivity')
    
    context ={'integralActivity':ma, 'form':form}
    return render(request, "createObjective.html", context)

#UPDATE OBJECTIVE
def updateObjective(request, pk):
    IA = Objective.objects.all()
    ma = Objective.objects.get(id=pk)
    form = ObjectiveForm(instance=ma)

    if request.method == 'POST':
        form = ObjectiveForm(request.POST, instance=ma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('objective')

    context = {'form': form, 'objective':IA}
    return render(request, "updateObjective.html", context)


#DELETE OBJECTIVE
def deleteObjective(request, pk):
    ma = objective.objects.get(id=pk)
    if request.method == 'POST':
        ma.delete()
        messages.success(request, 'Deleted successfully')
        return redirect('objective')
    
    context = {'item':ma}
    return render(request, "deleteObjective.html", context)

#INHERENT RISK
def inherentRisk(request):
    IR = InherentRisk.objects.all()
    form = InherentRiskForm(request.POST or None, request.FILES or None)
      
    if form.is_valid():
        form.save()
        messages.success(request, 'Saved successfully')
        return redirect('inherentRisk')
  
    context ={'inherentRisk':IR, 'form':form}
    return render(request, "inherentRisk.html", context)

#CREATE RISK
def createRisk(request, pk):
    IFormSet = inlineformset_factory(Objective, InherentRisk, fields=('objective', 'name'), extra=5)
    
    ma = Objective.objects.get(id=pk) 
    # create object of form
    form = IFormSet(queryset=InherentRisk.objects.none(), instance=ma)
    if request.method == 'POST':
        form = IFormSet(request.POST, instance=ma)
    # check if form data is valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved successfully')
            return redirect('objective')
    
    context ={'objective':ma, 'form':form}
    return render(request, "createRisk.html", context)

    
#UPDATE INHERENTRISK
def updateInherentRisk(request, pk):
    IR = InherentRisk.objects.all()
    ma = InherentRisk.objects.get(id=pk)
    form = InherentRiskForm(instance=ma)

    if request.method == 'POST':
        form = InherentRiskForm(request.POST, instance=ma)
        if form.is_valid():
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
