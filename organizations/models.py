from django.db import models

#User model
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True
    
    
class Organization(BaseModel):
    name = models.CharField(max_length=100)
    address = models.TextField()
    is_main = models.BooleanField()
    
    def __str__(self) -> str:
        return self.name
    

class Role(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    

class UserExtend(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.user.username
    
    
class Task(BaseModel):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    task_detail = models.TextField()