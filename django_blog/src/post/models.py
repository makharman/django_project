
from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    mobile_phone = models.CharField(max_length=12)
    user = models.OneToOneField(to=User, related_name='account', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)



class Post(models.Model):
    title = models.CharField(max_length=128)
    # photo = models.ImageField('post/imgs/', null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_actual = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')
    categories = models.ManyToManyField(to='Category',related_name='posts')
    
    class Meta:
        ordering = ['-updated_at']
     
    def __str__(self) -> str:
        return f'{self.id} - {self.title}'  
    
class Category(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_actual = models.BooleanField(default=False)  
    
    
    class Meta:
        db_table='categories'
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return f'{self.id} - {self.title}'   
    
    
      
      
# python manage.py makemigrations
# python manage.py migrate
# from post.models import Post
# python manage.py shell 
# exit() => выход из шелла

# from post.models import Post

# Post.objecst. =>
# all()
# filter(is_actual=True) => WHERE
# get(id=3) => возвращает 1 объект

# .filter(***__gt=3) (больше чем)
# .filter(***__gte=3) (больше или ровно чем)
# .filter(***__lt=3) (меньше чем)
# .filter(***__lte=3) (меньше или ровно чем)