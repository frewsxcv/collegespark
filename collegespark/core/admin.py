from django.contrib import admin
from collegespark.core.models import User


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
