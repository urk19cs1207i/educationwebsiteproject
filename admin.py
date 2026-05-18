from django.contrib import admin
from app1.models import Employee
from app1.models import Parent
from app1.models import Contact

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'ecity'] 

admin.site.register(Employee, EmployeeAdmin)

class ParentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message', 'studentname', 'email']

admin.site.register(Parent,ParentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message', 'email']

admin.site.register(Contact,ContactAdmin)

