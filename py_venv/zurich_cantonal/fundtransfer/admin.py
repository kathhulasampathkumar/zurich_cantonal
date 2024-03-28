from django.contrib import admin

# Register your models here.

from django.urls import reverse
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("ZURICH CANTONAL")
admin.site.site_title = _("ZURICH FUNDS  ADMINISTRATION SYSTEM")
admin.site.index_title = _("ZURICH FUNDS  ADMINISTRATION SYSTEM") # DASHBOARD NAME 


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(pk=request.user.pk)

    def balance(self, obj):
        # Assuming balance is a field in the User model, replace it with the actual field name
        return obj.balance
    balance.short_description = 'Balance'

# Unregister the old UserAdmin
admin.site.unregister(User)

# Register the User model with the CustomUserAdmin
admin.site.register(User, CustomUserAdmin)

# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

# class CustomUserAdmin(UserAdmin):
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(pk=request.user.pk)

#     # def has_change_permission(self, request, obj=None):
#     #     if obj is not None and not request.user.is_superuser:
#     #         return obj == request.user
#     #     return super().has_change_permission(request, obj)

# # Unregister the existing UserAdmin
# admin.site.unregister(User)

# # Register the UserAdmin with the custom queryset
# admin.site.register(User, CustomUserAdmin)


