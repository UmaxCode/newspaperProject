from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from django.contrib.admin import ModelAdmin

from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)

from .models import CustomUser, TodoItem

# Register your models here.

class CustomUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

class TodoAdmin(ModelAdmin):

    list_display = (
        'id', 'item_name', 'by_user'
    )

    


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(TodoItem, TodoAdmin)




