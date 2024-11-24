from django.shortcuts import render, redirect

#decorators
from django.contrib.auth.decorators import login_required

#access level check decorator
from .access import role_required

#logout
from django.contrib.auth import logout

#models
from .models import *

#forms
from .forms import OrganizationForm, UserForm, UserExtendForm, UserUpdateForm, TaskForm


# Create your views here.

#login homepage
def home_page(request):
    return render(request, 'organization/index.html', {})

#logout
def logout_view(request):
    logout(request)
    return render(request, 'organization/logout.html', {})


#all CRUD operations
#organization views

#list of organizations that are created
@login_required
@role_required(['ceo'])
def organization_list_view(request):
    organizations = Organization.objects.all()
    return render(request, 'organization/organization_list.html', {'organizations': organizations})

#create sub-organizations
@login_required
@role_required(['ceo'])
def organization_create_view(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organization_list')
    else:
        form = OrganizationForm()
    return render(request, 'organization/organization_form.html', {'form': form})

#update sub-organizations
@login_required
@role_required(['ceo'])
def organization_update_view(request, pk):
    organization = Organization.objects.get(id=pk)
    
    form = OrganizationForm(request.POST or None, instance=organization)
    
    if form.is_valid():
        form.save()
        return redirect('organization_list')
    return render(request, 'organization/organization_form.html', {'form': form})

#delete sub-organizations
@login_required
@role_required(['ceo'])
def organization_delete_view(request, pk):
    organization = Organization.objects.get(id=pk)
    organization.delete()
    return redirect('organization_list')

#users views

#list of users in organization
@login_required
@role_required(['ceo','chairman'])
def user_list_view(request):
    #here I have taken the login user role name
    role_name = str(UserExtend.objects.get(user = request.user).role)
    
    #based on the role I have filtered the data
    #for 'ceo' it will exclude the ceo's data so that the ceo can't or delete his account and also he cannot access the same level users as ceo's
    #same for chairman as the chairman he's level of athority is below the ceo so he cannot have access to above level and also same level users.
    if role_name == 'ceo':
        user_profile = UserExtend.objects.select_related('user', 'role').exclude(role__name='ceo')
    else:
        user_profile = UserExtend.objects.select_related('user', 'role').exclude(role__name='ceo').exclude(role__name='chairman')
    return render(request, 'organization/user_list.html', {'user_profile': user_profile})

#create users
@login_required
@role_required(['ceo'])
def user_create_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_extend_form = UserExtendForm(request.POST)
        
        if user_form.is_valid() and user_extend_form.is_valid():
            user = user_form.save()
            user_extend = user_extend_form.save(commit=False)
            user_extend.user = user
            user_extend.save()
            return redirect('user_list')
    else:
        user_form = UserForm()
        user_extend_form = UserExtendForm()
    return render(request, 'organization/user_form.html', {'user_form': user_form, 'user_extend_form': user_extend_form})

#update users
@login_required
@role_required(['ceo'])
def user_update_view(request, pk):
    user = User.objects.get(id=pk)
    user_extend = UserExtend.objects.get(user=user)
    
    user_form = UserUpdateForm(request.POST or None, instance=user)
    user_extend_form = UserExtendForm(request.POST or None, instance=user_extend)
    
    if user_form.is_valid() and user_extend_form.is_valid():
        user = user_form.save()
        user_extend = user_extend_form.save(commit=False)
        user_extend.user = user
        user_extend.save()
        return redirect('user_list')
    return render(request, 'organization/user_form.html', {'user_form': user_form, 'user_extend_form': user_extend_form})

#delete users
@login_required
@role_required(['ceo'])
def user_delete_view(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('user_list')

#task views

#task list
#Here associate has only access to view the task's that assigned to him
@login_required
@role_required(['ceo', 'chairman', 'associate'])
def task_list_view(request):
    #here I have taken the login user role name
    role_name = str(UserExtend.objects.get(user = request.user).role)
    
    #by using role name I have filtered the data
    #for associate he can only see the task's assigned to him
    #for above level users like ceo and chairman, they can see the all tasks assigned to all
    if role_name == 'associate':
        task = Task.objects.filter(username = request.user)
    else:
        task = Task.objects.all()
    
    return render(request, 'organization/task_list.html', {'task': task})

#task create
@login_required
@role_required(['ceo', 'chairman'])
def task_create_view(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('task_list')
    else:
        task_form = TaskForm()
    return render(request, 'organization/task_form.html', {'task_form': task_form})

#task update
@login_required
@role_required(['ceo', 'chairman'])
def task_update_view(request, pk):
    task = Task.objects.get(id=pk)
    
    task_form = TaskForm(request.POST or None, instance=task)
    
    if task_form.is_valid():
        task_form.save()
        return redirect('task_list')
    return render(request, 'organization/task_form.html', {'task_form': task_form})

#task delete
@login_required
@role_required(['ceo', 'chairman'])
def task_delete_view(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')