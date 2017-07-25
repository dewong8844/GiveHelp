from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ServiceType(models.Model):
    description = models.CharField(max_length=200, blank=True)
    car_needed = models.BooleanField(default=False)

    def __str__(self):
        return 'Service Type: ' + self.description

class Profile(models.Model):
    SENIOR = 'SR'
    VOLUNTEER = 'VR'
    BOTH = 'BH'
    USER_TYPE_CHOICES = (
        (SENIOR, 'Senior'),
        (VOLUNTEER, 'Volunteer'),
        (BOTH, 'Both'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES,
                                 default=SENIOR, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    driver_license = models.CharField(max_length=20, blank=True)
    driver_license_state = models.CharField(max_length=2, blank=True)
    car_license_plate = models.CharField(max_length=20, blank=True)
    car_license_state = models.CharField(max_length=2, blank=True)
    photo = models.ImageField(upload_to='profile', blank=True)
    home_address = models.CharField(max_length=100, blank=True)
    home_city = models.CharField(max_length=30, blank=True)
    home_state = models.CharField(max_length=2, blank=True)
    home_zipcode = models.CharField(max_length=9, blank=True)
    service_types = models.ManyToManyField(ServiceType, blank=True) 
    has_disability = models.BooleanField(default=False)

    def __str__(self):
        return 'User name: ' + self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Service(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    datetime = models.DateField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    HOME = 'HOME'    # Service Location is at home
    TRIP = 'TRIP'    # Trip is from home to a destination address
    OTHER = 'OTHER'
    LOCATION_CHOICES = (
        (HOME, 'Home'),
        (TRIP, 'Trip'),
        (OTHER, 'Other'),
    )
    location = models.CharField(max_length=5, choices=LOCATION_CHOICES,
                                 default=HOME)
    NEW = 'NEW'     # Service "ticket" just created
    ASD = 'ASD'
    CMD = 'CMD'
    STATUS_CHOICES = (
        (NEW, 'New'),
        (ASD, 'Assigned'),
        (CMD, 'Completed'),
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES,
                                 default=NEW)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zipcode = models.CharField(max_length=9, blank=True)
    urgency = models.CharField(max_length=100, blank=True)
    special_instructions = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return 'Service type: ' + self.service_type.description + ' for ' + self.profile.user.username
