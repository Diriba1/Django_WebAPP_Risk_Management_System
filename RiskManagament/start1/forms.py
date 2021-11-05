from .models import InherentRisk, IntegralActivity, MajorActivity, Objective, CustomUser
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AdminDateWidget


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'working_Place']



class MajorActivityForm(forms.ModelForm):
    class Meta:
        model = MajorActivity
        fields = '__all__'
        widgets = {'added_by': forms.HiddenInput()}

class IntegralActivityForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(IntegralActivityForm, self).__init__(*args, **kwargs)
        self.fields['major_Activity'].queryset = MajorActivity.objects.filter(added_by=user)

    class Meta:
        model = IntegralActivity
        fields = '__all__'
        widgets = {'added_by': forms.HiddenInput()}

class ObjectiveForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ObjectiveForm, self).__init__(*args, **kwargs)
        self.fields['integral_Activity'].queryset = IntegralActivity.objects.filter(added_by=user)

    class Meta:
        model = Objective
        fields = '__all__'
        widgets = {'added_by': forms.HiddenInput()}

class InherentRiskForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(InherentRiskForm, self).__init__(*args, **kwargs)
        self.fields['objective'].queryset = Objective.objects.filter(added_by=user)
        
    class Meta:
        model = InherentRisk
        fields = ['objective', 'name','level', 'it_System', 'privilage', 'procedure_Manual', 'maker_Checker', 'dual_Control', 'frequency_of_Exposure', 'monetary_Value', 'risk_Condition']
        widgets = {'level': forms.HiddenInput()}
        

class InherentRiskNameForm(forms.ModelForm):
    class Meta:
        model = InherentRisk
        fields = ['name', 'added_by']
        widgets = {'added_by': forms.HiddenInput()}

class RmcdUserForm(forms.ModelForm):
    class Meta:
        model = InherentRisk
        fields = ['name','risk_Mitigation', 'risk_Catagory', 'owner', 'target_Completion', 'management_Plan']
        widgets = {
        'target_Completion': forms.DateInput(attrs=dict(type='date'))
    }

class IadUserForm(forms.ModelForm):
    class Meta:
        model = InherentRisk
        fields = ['name', 'unrectified_Audit_Findings']