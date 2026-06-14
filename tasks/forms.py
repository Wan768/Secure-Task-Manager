import magic
from django import forms
from .models import Task
from django.core.validators import RegexValidator
from django.core.files.uploadedfile import UploadedFile

class TaskForm(forms.ModelForm):
    # Regex (Whitelisting): Only letters, numbers, and spaces allowed
    # prevents malicious scripts or unexpected characters
    title_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9\s]+$',
        message="Title must only contain alphanumeric characters and spaces.",
        code='invalid_title'
    )

    title = forms.CharField(validators=[title_validator], max_length=100)

    class Meta:
        model = Task
        # Updated to match the fields
        fields = ['title', 'description', 'status', 'deadline', 'uploaded_file']
        
        # calendar picker
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }
        
    # Server-side validation
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) < 5:
            raise forms.ValidationError("Description is too short. Please be more specific.")
        return description

    # Secure File Upload Validation (MIME & Extension)
    def clean_uploaded_file(self):
        file = self.cleaned_data.get('uploaded_file')
        
        # No file uploaded (Allowed)
        if not file:
            return file
        
        if not isinstance(file, UploadedFile):
            return file

        # Set what file is allowed on your system
        allowed_mimes = ['application/pdf', 'image/jpeg', 'image/png']
        allowed_extensions = ['pdf', 'jpg', 'jpeg', 'png']

        # Check Extension
        ext = file.name.split('.')[-1].lower()
        if ext not in allowed_extensions:
            raise forms.ValidationError(f"Unsupported file extension. Allowed: {', '.join(allowed_extensions)}")

        # Check actual MIME type 
        # Read the first 2048 bytes of the file to check its true identity
        file_mime = magic.from_buffer(file.read(2048), mime=True)
        if file_mime not in allowed_mimes:
            raise forms.ValidationError("File contents do not match allowed types.")
            
        # Reset the file reader pointer so Django can save it properly
        file.seek(0)
        
        return file