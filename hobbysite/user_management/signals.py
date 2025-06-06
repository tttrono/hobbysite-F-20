from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """ auto-create profile after sign-up."""
    if created:
        Profile.objects.create(user=instance, email=instance.email) 

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()