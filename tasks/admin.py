from django.contrib import admin
from .models import Task, FailedLoginAttempt

# Admin CRUD tasks for all user
admin.site.register(Task)


class FailedLoginAttemptAdmin(admin.ModelAdmin):
    
    list_display = ('username', 'ip_address', 'timestamp')
    
    search_fields = ('username', 'ip_address')
   
    list_filter = ('timestamp',)
    
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(FailedLoginAttempt, FailedLoginAttemptAdmin)


