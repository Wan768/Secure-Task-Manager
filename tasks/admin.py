from django.contrib import admin
from .models import Task, FailedLoginAttempt

# Admin CRUD tasks for all user
admin.site.register(Task)

# creates a customized  grid for the security logs
class FailedLoginAttemptAdmin(admin.ModelAdmin):
    # The columns the admin will see
    list_display = ('username', 'ip_address', 'timestamp')
    # Adds a search bar to look up specific attempts
    search_fields = ('username', 'ip_address')
    # filter by date
    list_filter = ('timestamp',)
    
    # Make the logs read-only 
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(FailedLoginAttempt, FailedLoginAttemptAdmin)


