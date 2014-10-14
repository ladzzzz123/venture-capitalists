from django.contrib import admin
from company_directory.models import Company
from company_directory.models import State


class CompanyAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'phone', 'address', 'city', 'state', 'zip']

admin.site.register(Company, CompanyAdmin)
admin.site.register(State)
