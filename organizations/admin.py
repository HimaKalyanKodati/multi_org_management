from django.contrib import admin

#models
from .models import *

# Register your models here.

admin.site.register([Organization, Role, UserExtend, Task])