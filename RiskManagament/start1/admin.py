from django.contrib import admin
from .models import MajorActivity, IntegralActivity, Objective, InherentRisk, Branch


admin.site.site_header = "Admin"
admin.site.site_title = " Admin Area"
admin.site.index_title = " admin area"

admin.site.register(MajorActivity)
admin.site.register(IntegralActivity)
admin.site.register(Objective)
admin.site.register(InherentRisk)
admin.site.register(Branch)

