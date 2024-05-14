from django.apps import AppConfig
import os
from django.conf import settings


class PressServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'press_service'
    path = os.path.join(settings.BASE_DIR, 'press_service')