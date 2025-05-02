from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class Profile(models.Model):
    """ A model for user profile. """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    display_name = models.CharField(max_length=63, default='')
    email = models.EmailField(max_length=254, unique=True, default='')
    
    def _str_(self):
        #return self.display_name
        return self.display_name
    
    def get_absolute_url(self):
        return reverse('profile', args=[self.pk])
        #return reverse('profile')

