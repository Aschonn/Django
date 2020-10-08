
from django.db.models.signals import post_save
from django.contrib.auth.models import User
#function that gets signal and runs function
from django.dispatch import receiver
#import profile model
from .models import Profile

#main goal is to create a profile for each user
#kwargs accepts additional keyword or parameters
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
            #sends user form data to Profile Model in models.py
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()