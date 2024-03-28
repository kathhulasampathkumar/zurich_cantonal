from django.contrib import admin

# Register your models here.
from user_master.models import user_master
class UserMasterAdmin(admin.ModelAdmin):    
    list_display = ('username','email','contact', 'balance','user_type','status') 
    class Meta:
        verbose_name = 'profile'  # Set the custom verbose name   
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user:
            return qs
        return qs.filter(pk=request.user.pk)
admin.site.register(user_master, UserMasterAdmin)

