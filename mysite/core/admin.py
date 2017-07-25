from django.contrib import admin
from core.models import ServiceType
from core.models import Service
from core.models import Profile

admin.site.register(ServiceType)
admin.site.register(Service)
admin.site.register(Profile)
