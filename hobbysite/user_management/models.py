from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class Profile(models.Model):
    """ A model for user profile. """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=63, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    
    def _str_(self):
        return self.display_name
    
    def get_absolute_url(self):
        return reverse('profile', args=[self.pk])
        #return reverse('profile')
