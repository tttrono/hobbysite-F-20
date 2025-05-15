from django.db import models
from django.urls import reverse
from enum import unique

from user_management.models import Profile

class Commission(models.Model):
    """A model for commissions."""
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='commission')
    
    class Status(models.TextChoices):
         OPEN = 'open', 'Open'
         FULL = 'full', 'Full'
         COMPLETED = 'completed', 'Completed'
         DISCONTINUED = 'discontinued', 'Discontinued'
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Commissions'
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
         return reverse('commissions:detail', args=[self.pk])
     
class Job(models.Model):
    """A model for job."""
    commission = models.ForeignKey(Commission, null=False, on_delete=models.CASCADE, related_name='jobs')
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    
    class Status(models.TextChoices):
        OPEN = 'open', 'Open'
        FULL = 'full', 'Full'
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)

    class Meta:
        verbose_name_plural = 'Jobs'
        ordering = ['-status','-manpower_required','role']
        
    def __str__(self):
        return f"{self.role} for {self.commission.title}"
    
    # def get_absolute_url(self):
    #      return reverse('commissions:detail', args=[self.pk])

class JobApplication(models.Model):
    """A model for job application. """
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='applications')
    
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        ACCEPTED = 'accepted', 'Accepted'
        REJECTED = 'rejected', 'Rejected'
        
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    applied_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Job Applications'
        ordering = ['-applied_on']
     
