from django.contrib import admin
from .models import Authentication


class AuthenticationModel(admin.ModelAdmin):
    list_display = ['email', 'password', 'withPic']


admin.site.register(Authentication, AuthenticationModel)
