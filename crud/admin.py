from django.contrib import admin
from . models import Employee
from . models import Login
from . models import Drop
from . models import Dropform
# Register your models here.
admin.site.register(Employee)
admin.site.register(Login)
admin.site.register(Drop)
admin.site.register(Dropform)