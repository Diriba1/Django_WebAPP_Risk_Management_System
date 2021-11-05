from django.contrib import admin
from .models import WorkUnit, CustomUser, MajorActivity, IntegralActivity, InherentRisk

admin.site.site_header = "Admin"
admin.site.site_title = " Admin Area"
admin.site.index_title = " admin area"

admin.site.register(CustomUser)
admin.site.register(WorkUnit)
# admin.site.register(MajorActivity)
admin.site.register(InherentRisk)
# admin.site.register(IntegralActivity)

