from django.contrib import admin
from .models import WorkUnit, CustomUser

admin.site.site_header = "Admin"
admin.site.site_title = " Admin Area"
admin.site.index_title = " admin area"

admin.site.register(CustomUser)
admin.site.register(WorkUnit)

