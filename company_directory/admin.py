from django.contrib import admin
from company_directory.models import Company
from company_directory.models import State


class CompanyAdmin(admin.ModelAdmin):
    fields = ['logo', 'name', 'email', 'phone', 'address', 'city', 'state', 'zip']
    list_display = ('logo_tag', 'name',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(State)
