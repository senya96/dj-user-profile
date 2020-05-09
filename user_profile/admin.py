from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'bio', 'birth_date', 'location', 'email']
    list_display = ['username', 'bio', 'birth_date', 'location', 'email']


admin.site.register(User, UserAdmin)
