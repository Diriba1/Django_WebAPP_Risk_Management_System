from django.db import models

# Create your models here.

class Branch(models.Model):
    TYPE = (('Office', 'Office'), ('Department', 'Department'), ('Branch', 'Branch'))
    type = models. CharField(max_length=30, choices=TYPE)
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MajorActivity(models.Model):
    name = models.CharField(max_length=300)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class IntegralActivity(models.Model):
    majorActivity = models.ForeignKey(MajorActivity, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Objective(models.Model):
    integralActitivty = models.ForeignKey(IntegralActivity, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class InherentRisk(models.Model):
    
    RISKCATAGORY = (('Financial','Financial'),('Reputational','Reputational'),('Marketing','Marketing'),('Legal','Legal'),)
    PROCEDURALMANUAL = (('Available', 'Available'), ('NA', 'NA'),)
    MAKERCHECKER = (('Available', 'Available'), ('NA', 'NA'),)
    DUALCONTROL = (('Available', 'Available'), ('NA', 'NA'),)
    FREQUENCYOFEXPOSURE =(('Daily', 'Daily'),('Weekly', 'Weekly'),('Monthly', 'Monthly'),('Quarterly', 'Quarterly'),('Semi Anually', 'Semi Anually'),('Anually', 'Anually'),)
    RISKCONDITION = (('Reversible', 'Reversible'), ('Irreversible', 'Irreversible'),)
    CONSEQUENCY = (('Insignificant', 'Insignificant'), ('Moderate', 'Moderate'), ('Major', 'Major'), ('Catastrophic', 'Catastrophic'),)
    RISKMITIGATION = (('Tolerate', 'Tolerate'), ('Treat', 'Treat'), ('Transfer', 'Transfer'), ('Terminate', 'Terminate'),)
    UNRECTIFIEDAUDITFINDING = (('Found', 'Found'), ('Not Found', 'Not found'))


    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, null=False, blank=True)
    name = models.CharField(max_length=300,null=False, blank=True)
    riskCatagory = models.CharField(max_length=30, choices = RISKCATAGORY, null=False, blank=True)
    procedureManual = models.CharField(max_length=30, choices = PROCEDURALMANUAL, null=False, blank=True)
    makerChecker = models.CharField(max_length=30, choices = MAKERCHECKER, null=False, blank=True)
    dualControl = models.CharField(max_length=30, choices = DUALCONTROL, null=False, blank=True)
    frequencyofExposure = models.CharField(max_length=30, choices = FREQUENCYOFEXPOSURE, null=False, blank=True)
    riskCondition = models.CharField(max_length=30, choices = RISKCONDITION, null=False, blank=True)
    consequence = models.CharField(max_length=30, choices = CONSEQUENCY, null=False, blank=True)

    riskMitigation = models.CharField(max_length=30, choices=RISKMITIGATION, null=False, blank=True)
    owner = models.CharField(max_length=300,null=False, blank=True)
    targetCompletion = models.CharField(max_length=300, null=False, blank=True)
    status = models.CharField(max_length=300, null=False, blank=True)

    unrectifiedAuditFindings = models.CharField(max_length=30, choices=UNRECTIFIEDAUDITFINDING, null=False, blank=True)

    def __str__(self):
        return self.name
