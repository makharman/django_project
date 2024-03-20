from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    status_choices = (
        ('ACTIVE', 'Active'),
        ('DRAFT', 'Draft'),
    )
    
    title = models.CharField(verbose_name='Заголовок поста', max_length=255)
    text = models.TextField(verbose_name='Текст поста', max_length=2048)
    status = models.CharField(
        verbose_name='Статус поста',
        max_length=6, 
        choices=status_choices, 
        default='DRAFT'
    )
    
    image = models.ImageField(
        verbose_name='Изображение поста', 
        upload_to='imgs/posts', 
        null=True, 
        blank=True
    )
    
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, null=True)
    is_active = models.BooleanField(default=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_posts')
    
    categories = models.ManyToManyField('Category', related_name='api_posts')
    
    class Meta:
        ordering = ['-updated_at']
     
    def __str__(self):
        return f'{self.id} - {self.title}'  

class Category(models.Model):
    title = models.CharField(
        verbose_name='Название категории',
        max_length=128,
        unique=True,
    )
    
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, null=True)
    is_active = models.BooleanField(verbose_name='Статус категории', default=False)  
    
    class Meta:
        db_table = 'api_categories'
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.id} - {self.title}'   

    
    