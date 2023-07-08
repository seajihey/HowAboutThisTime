from django.contrib import admin

# Register your models here.
from .models import User, Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ["group_name", "group_code"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "pw", "name", "email", "img"]


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
