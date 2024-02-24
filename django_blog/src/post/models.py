import random
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=128, null=True, default=f'post {int(random.random() * 100)}')
    photo = models.ImageField('post/imgs/', null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_actual = models.BooleanField(blank=True, null=True)
    
    
    
