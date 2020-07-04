from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    # user alredy have fields: username, first&last name,
    #email, password, groups, is_superuser, date_joined
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.TextField(max_length=500, blank=True)
    userType = models.TextField(max_length=100, blank=True)
    supplyType = models.TextField(max_length=100, blank=True)
    supplyNumber = models.TextField(max_length=30, blank=True)
    addr = models.TextField(max_length=500, blank=True)
    tel = models.TextField(max_length=500, blank=True)
    info = models.TextField(max_length=500, blank=True)

# define signals - Profile model will be automatically created/updated when we create/update a User instance.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
