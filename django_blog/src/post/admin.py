from django.contrib import admin
from .models import Post, Category,UserAccount


@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at', 'is_actual']
    readonly_fields = (
        'created_at',
        'updated_at',
    )
@admin.register(Category)  
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_actual')
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    
@admin.register(UserAccount)  
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id','created_at', 'updated_at','mobile_phone')
    readonly_fields = (
        'created_at',
        'updated_at',
    )