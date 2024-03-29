from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from .models import User


@register(User)
class MyUserAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
    )
    fields = (
        (
            "username",
            "email",

        ),
        (
            "first_name",
            "last_name",
        ),
    )
    fieldsets = []

    search_fields = (
        "username",
        "email",
    )
    list_filter = (
        "first_name",
        "email",
    )
    save_on_top = True
