#forms
from django import forms
from django.contrib.auth.forms import UserCreationForm

#models
from .models import Organization, UserExtend, Task
from django.contrib.auth.models import User


#organization create/update form
class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'


#user create form     
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


#extended user create/update form
class UserExtendForm(forms.ModelForm):
    class Meta:
        model = UserExtend
        fields = ['role', 'organization']
        

#user update form      
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        

#task create/update form  
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
