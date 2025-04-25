from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    """ A model for user profile. """
    user = models.OneToOneField(User, one_delete=models.CASCADE)
    display_name = models.CharField(max_length=63)
    email = models.EmailField(max_length=254)
    
    def _str_(self):
        return self.name
