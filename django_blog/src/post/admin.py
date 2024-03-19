from django.contrib import admin
from .models import Post, Category


@admin.register(Post) 
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at', 'is_active']
    readonly_fields = (
        'created_at',
        'updated_at',
    )
@admin.register(Category)  
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_active')
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    
