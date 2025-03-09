from django.db import models

from django.db import models
from django.urls import reverse
from enum import unique

class Commission(models.Model):
    """A model for commissions."""
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    people_required = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Commissions'
        ordering = ['created_on']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
         return reverse('commissions:detail', args=[self.id])

class Comment(models.Model):
    """A model for comments on commissions."""
    commission = models.ForeignKey(Commission, null=False, on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['-created_on']
        
    # def __str__(self):
    #     return self.name


