from django.contrib import admin
from .models import UserAccount

@admin.register(UserAccount)  
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id','created_at', 'updated_at','mobile_phone')
    readonly_fields = (
        'created_at',
        'updated_at',
    )
