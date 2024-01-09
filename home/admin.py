# home/admin.py

from django.contrib import admin
from home.models import District, Branch, AccountType, Material, UserProfile

# Register your models here.
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(AccountType)
admin.site.register(Material)
admin.site.register(UserProfile)
