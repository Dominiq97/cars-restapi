from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models


admin.site.register(models.Car)
admin.site.register(models.Rate)
