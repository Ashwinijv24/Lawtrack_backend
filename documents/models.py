
from django.db import models
from cases.models import Case

class Document(models.Model):
    DOCUMENT_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('pdf', 'PDF'),
        ('other', 'Other'),
    ]
    
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=200, default='Untitled Document')
    file = models.FileField(upload_to='documents/')
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES, default='other')
    description = models.TextField(blank=True, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.case.title}"
