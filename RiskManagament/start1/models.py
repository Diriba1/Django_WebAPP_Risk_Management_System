from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.conf import settings
from django import forms



class WorkUnit(models.Model):
    TYPE = (('Office', 'Office'), ('Department', 'Department'), ('Branch', 'Branch'))
    type = models. CharField(max_length=30, choices=TYPE)
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    working_Place = models.ForeignKey(WorkUnit, null=True, blank=True, on_delete=models.CASCADE)
    is_Rmcd_User = models.BooleanField(default=False)
    is_Iad_USer = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class MajorActivity(models.Model):
    name = models.CharField(max_length=300)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class IntegralActivity(models.Model):
    major_Activity = models.ForeignKey(MajorActivity, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Objective(models.Model):
    integral_Activity = models.ForeignKey(IntegralActivity, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class InherentRisk(models.Model):
    
    RISKCATAGORY = (('Financial','Financial'),('Reputational','Reputational'),('Marketing','Marketing'),('Legal','Legal'),)
    CHOICES = (('AV', 'Available'), ('NA', 'Not Available'),)
    FREQUENCYOFEXPOSURE =(('Daily', 'Daily'),('Weekly', 'Weekly'),('Monthly', 'Monthly'),('Quarterly', 'Quarterly'),('Semi Anually', 'Semi Anually'),('Anually', 'Anually'),)
    RISKCONDITION = (('Tolerable', 'Tolerable'), ('Reversible', 'Reversible'), ('costly', 'Costly Reversible'), ('Unreversible', 'Unreversible'))
    RISKMITIGATION = (('Tolerate', 'Tolerate'), ('Treat', 'Treat'), ('Transfer', 'Transfer'), ('Terminate', 'Terminate'),)

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, null=False, blank=True)
    name = models.CharField(max_length=300,null=False, blank=True)
    risk_Catagory = models.CharField(max_length=30, choices = RISKCATAGORY, null=False, blank=True)
    it_System = models.CharField(max_length=30, choices = CHOICES, null=False, blank=True)
    privilage = models.CharField(max_length=30, choices = CHOICES, null=False, blank=True)
    procedure_Manual = models.CharField(max_length=30, choices = CHOICES, null=False, blank=True)
    maker_Checker = models.CharField(max_length=30, choices = CHOICES, null=False, blank=True)
    dual_Control = models.CharField(max_length=30, choices = CHOICES, null=False, blank=True)
    frequency_of_Exposure = models.CharField(max_length=30, choices = FREQUENCYOFEXPOSURE, null=False, blank=True)
    monetary_Value = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    risk_Condition = models.CharField(max_length=30, choices = RISKCONDITION, null=False, blank=True)
    
    risk_Mitigation = models.CharField(max_length=30, choices=RISKMITIGATION, null=False, blank=True)
    owner = models.CharField(max_length=300,null=False, blank=True)
    target_Completion = models.CharField(max_length=300, null=False, blank=True)
    status = models.CharField(max_length=300, null=False, blank=True)

    unrectified_Audit_Findings = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def level_word(self):
        if self.level == 1:
            return "Low"
        elif self.level == 2:
            return "Moderate"
        elif self.level == 3:
            return "Significant"
        elif self.level == 4:
            return "High"
        elif self.level == 5:
            return "Extreme"
        else:
            return "None"

    def score(self):
        if self.unrectified_Audit_Findings and self.level and self.level!=666:
            return self.unrectified_Audit_Findings * self.level
        else:
            return -1