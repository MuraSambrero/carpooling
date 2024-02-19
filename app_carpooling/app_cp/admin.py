from django.contrib import admin
from .models import Trip, User, CityA, CityB, Car
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

UserAdmin.fieldsets = (
    (None, {'fields': ('username', 'password')}),
    (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'tel', 'car')}),
    (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    'groups', 'user_permissions')}),
    (_('Important dates'), {'fields': ('last_login',)}))

admin.site.register(User, UserAdmin)
admin.site.register(Trip)
admin.site.register(CityA)
admin.site.register(CityB)
admin.site.register(Car)
