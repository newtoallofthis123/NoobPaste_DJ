from django.contrib import admin

# Register your models here.

from .models import AuthModel

admin.register.site(AuthModel)