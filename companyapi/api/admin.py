from django.contrib import admin
from api.models import Company, Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location')
    search_fields = ('name', 'type')
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company', 'email', 'phone')
    search_fields = ('name', 'position', 'email', 'phone')
    list_filter = ('company', 'position')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
