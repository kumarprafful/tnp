from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

# models
from .models import User, StudentProfile, FacultyProfile

# Register your models here.

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'enrollment_no')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_faculty', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important date'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_faculty')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(StudentProfile, search_fields=('enrollment_no', ))
admin.site.register(FacultyProfile,)
