import uuid
import os
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver

#Secure File Upload func
def secure_file_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('task_files/', new_filename)

def validate_file_size(file):
    max_size_mb = 5
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"File size exceeds the {max_size_mb}MB limit.")


class Task(models.Model):
    STATUS_CHOICES = (
        ('To do', 'To do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To do')
    
    uploaded_file = models.FileField(
        upload_to=secure_file_path, 
        validators=[validate_file_size],
        blank=True, 
        null=True
    )
    
    deadline = models.DateField(blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['status']

class FailedLoginAttempt(models.Model):
    username = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Failed login: '{self.username}' at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    attempted_username = credentials.get('username', 'Unknown')
    
    ip = None
    if request:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            
    FailedLoginAttempt.objects.create(username=attempted_username, ip_address=ip)
