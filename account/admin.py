from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Create password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ("email",)
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField
    
    class Meta:
        model = User
        fields = ("email", "is_active", "is_staff", "is_admin")

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    search_fields = ("email",)
    list_display = ("email", "is_staff", "is_admin", "last_login")
    list_filter = ()
    filter_horizontal = ()
    ordering = ()
    
    fieldsets = (
        (None, {
            "fields": ("email", "password")
        }),
        ("Permission", {
            "fields": ("is_active", "is_staff", "is_admin")
        })
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
