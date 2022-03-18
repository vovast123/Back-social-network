from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'image',
                    'email',
                    'describe',
                )
            }
        )
    )

    # Edit user
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'image',
                    'describe',
                )
            }
        )
    )


admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Reviews)
admin.site.register(Folower)
admin.site.register(Message)