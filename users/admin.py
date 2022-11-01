from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms

class CustomUserChangeFrom(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields
        widgets = {
            'bio': forms.Textarea
        }
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeFrom
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'bio']
    fieldsets = UserAdmin.fieldsets + (
        ("User's Bio", {'fields': ('bio',)}),
    )
admin.site.register(User,CustomUserAdmin)