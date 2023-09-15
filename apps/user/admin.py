from django.contrib import admin

from apps.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'password', 'city', 'avatar', 'phone', 'telegram', 'role', 'is_superuser',)
    list_filter = ('email', 'first_name', 'last_name', 'role', 'is_superuser', 'city',)
    search_fields = ('email', 'first_name', 'last_name', 'city',)
