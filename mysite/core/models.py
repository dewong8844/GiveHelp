from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=40, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zipcode = models.CharField(max_length=9, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    help_status = models.CharField(max_length=100, blank=True)
    has_disability = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Service(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100, blank=True)
    datetime = models.DateField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    ride_needed = models.BooleanField(default=False)
    location = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    urgency = models.CharField(max_length=100, blank=True)
    special_instructions = models.TextField(max_length=1000, blank=True)
