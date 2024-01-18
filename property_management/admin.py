from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from property_management.models import (
   Property,
   Unit
)
admin.site.register(Property)
admin.site.register(Unit)



