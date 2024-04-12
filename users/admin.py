from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "is_admin",
        "profile_picture_thumbnail",
    )
    list_filter = ("is_admin",)
    fieldsets = (
        ("User Credentials", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "profile_picture")}),
        ("Permissions", {"fields": ("is_admin",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "profile_picture",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email", "id")
    filter_horizontal = ()

    def profile_picture_thumbnail(self, obj):
        if obj.profile_picture:
            return (
                '<img src="%s" style="width:100px;height:auto;" />'
                % obj.profile_picture.url
            )
        else:
            return "No Image"

    profile_picture_thumbnail.allow_tags = True
    profile_picture_thumbnail.short_description = "Profile Picture"


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
