from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Role
from .forms import UserRegisterForm
from django.contrib.auth import get_user_model
User = get_user_model()
# Register your models here.
class UsersAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password','email','role',),
        }),
    )

admin.site.register(User,UsersAdmin)
admin.site.register(Role)
