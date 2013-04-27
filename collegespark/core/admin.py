from django.contrib import admin
from collegespark.core.models import User, School, Major


class UserAdmin(admin.ModelAdmin):
    pass


class SchoolAdmin(admin.ModelAdmin):
    pass


class MajorAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Major, MajorAdmin)
