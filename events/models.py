
from django.db import models
from cases.models import Case

class Event(models.Model):
    EVENT_TYPES = [
        ('hearing', 'Court Hearing'),
        ('meeting', 'Client Meeting'),
        ('deadline', 'Deadline'),
        ('other', 'Other'),
    ]
    
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200, default='Untitled Event')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='hearing')
    date = models.DateTimeField()
    location = models.CharField(max_length=300, blank=True, default='')
    description = models.TextField(blank=True, default='')
    reminder_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return f"{self.title} - {self.date.strftime('%Y-%m-%d')}"
