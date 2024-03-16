from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    mobile_phone = models.CharField(max_length=12)
    user = models.OneToOneField(to=User, related_name='account', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        db_table='UserAccount'
        ordering = ['-created_at']
        verbose_name = 'UserAccount'
        verbose_name_plural = 'UserAccounts '

    def __str__(self) -> str:
        return f'{self.id} - {self.mobile_phone}'   
    