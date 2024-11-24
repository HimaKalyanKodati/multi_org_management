from django.urls import path

#login
from django.contrib.auth.views import LoginView

#views
from .views import *

urlpatterns = [
    #login home page
    path('', home_page, name='home_page'),
    #login and logout
    path('login/', LoginView.as_view(template_name = 'organization/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    #organization
    path('organization/list/', organization_list_view, name='organization_list'),
    path('organization/create/', organization_create_view, name='organization_create'),
    path('organization/update/<int:pk>/', organization_update_view, name='organization_update'),
    path('organization/delete/<int:pk>/', organization_delete_view, name='organization_delete'),
    #user
    path('user/list/', user_list_view, name='user_list'),
    path('user/create/', user_create_view, name='user_create'),
    path('user/update/<int:pk>/', user_update_view, name='user_update'),
    path('user/delete/<int:pk>/', user_delete_view, name='user_delete'),
    #task
    path('task/list/', task_list_view, name='task_list'),
    path('task/create/', task_create_view, name='task_create'),
    path('task/update/<int:pk>/', task_update_view, name='task_update'),
    path('task/delete/<int:pk>/', task_delete_view, name='task_delete'),
]
