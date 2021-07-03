from django.contrib import admin
from bankapp.models import Banking

class BankingAdmin(admin.ModelAdmin):
    list_display = ['c_name','c_id','c_phone_no','c_emailid','c_balance']

# Register your models here.
admin.site.register(Banking,BankingAdmin)
