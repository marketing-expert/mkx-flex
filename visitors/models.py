# visitors.models.py

import uuid

from django.db import models
from django.contrib.admin import widgets



class Visitor(models.Model):
    """
    Visitors database
    """
    
    GENDER_CHOICES = (
        ('Mr', 'Mr'),
        ('Mme', 'Mme'),
        ('Mlle', 'Mlle'),
    )

    uuid = models.UUIDField(
        db_index=True, default=uuid.uuid4,
        editable=False, verbose_name='UUID'
    )
    gender = models.CharField(
        max_length=4, default="Mr",
        choices=GENDER_CHOICES, verbose_name='civilité',
    )
    
    name = models.CharField(verbose_name="nom & prénoms", max_length=80)
    phone = models.CharField(verbose_name="téléphone", max_length=50)
    email = models.EmailField(verbose_name="adresse email", max_length=80)
    subject_visit = models.CharField(verbose_name="sujet de la visite", max_length=50)
    hour_start_visit = models.TimeField(verbose_name="heure d'arrivée", auto_now=False, auto_now_add=False)
    hour_end_visit = models.TimeField(verbose_name="heure de depart", auto_now=False, auto_now_add=False)
    created_at = models.DateField(verbose_name="date de création", auto_now=False, auto_now_add=True)

    class Meta:
        db_table = 'db_visitors'
        ordering = ('-created_at',)
        get_latest_by = ('-created_at',)
        verbose_name_plural = 'Visiteurs'
        indexes = [
            models.Index(fields=['id', 'uuid'], name='id_index_visitors'),
        ]
