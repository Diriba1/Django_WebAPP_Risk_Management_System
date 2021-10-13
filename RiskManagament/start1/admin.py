from django.contrib import admin
from .models import MajorActivity, IntegralActivity, Objective, InherentRisk, Branch
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

admin.site.site_header = "Admin"
admin.site.site_title = " Admin Area"
admin.site.index_title = " admin area"

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]

admin.site.register(CustomUser)
admin.site.register(MajorActivity)
admin.site.register(IntegralActivity)
admin.site.register(Objective)
admin.site.register(InherentRisk)
admin.site.register(Branch)

