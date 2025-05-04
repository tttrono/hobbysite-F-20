from django.db import models

from django.db import models
from django.urls import reverse
from enum import unique

class Commission(models.Model):
    """A model for commissions."""
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    
    class Status(models.TextChoices):
        OPEN = 'open', 'Open'
        FULL = 'full', 'Full'
        COMPLETED = 'completed', 'Completed'
        DISCONTINUED = 'discontinued', 'Discontinued'
        
    # STATUS_OPTIONS = (
    #     ('open', 'Open'),
    #     ('full', 'Full'),
    #     ('completed', 'Completed'),
    #     ('discontinued', 'Discontinued'),
    # )
    # status = models.CharField(max_length=20,choices=STATUS_OPTIONS, default='open')
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Commissions'
        ordering = ['created_on']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
         return reverse('commissions:detail', args=[self.pk])

class Comment(models.Model):
    """A model for comments on commissions."""
    commission = models.ForeignKey(Commission, null=False, on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['-created_on']
        
    def __str__(self):
        return f"Comment on {self.commission.title}" 



