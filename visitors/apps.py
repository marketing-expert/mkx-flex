# visitors.apps.py

from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save
from django.apps import AppConfig


class VisitorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visitors'
    label = 'visitors'
    verbose_name = 'visiteur'

    def ready(self):
        visitor = self.get_model('Visitor')
        pre_save.connect(receiver, sender=visitor)
