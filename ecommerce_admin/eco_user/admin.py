from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, MobileOtp


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email','first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name','password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'is_active')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)

class MobileOtpAdmin(admin.ModelAdmin):
    mobile = MobileOtp
    # list_display = ('email',)
    
admin.site.register(MobileOtp, MobileOtpAdmin)