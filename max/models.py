# max.models.py

import uuid
from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator

from flex.models import Visitor
from phonenumber_field.modelfields import PhoneNumberField


class Pack(models.Model):

    price = models.PositiveIntegerField(
        verbose_name="prix du pack",
        default=5000,
        validators=[
            MinValueValidator(5000),
            MaxValueValidator(800000)
        ],
        help_text="définir le prix du pack"
    )

    class Meta:
        db_table = 'db_packs'
        verbose_name_plural = 'packs'
        indexes = [
            models.Index(
                fields=['id'],
                name='id_packs'
            ),
        ]

    def __str__(self):
        return self.pack
    
    @admin.display(description="prix du pack")
    def get_pack_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse(
            "pack:pack_detail",
            kwargs={"pk": self.pk}
        )
    

class Souscriber(models.Model):

    uuid = models.UUIDField(
        db_index=True, default=uuid.uuid4,
        editable=False, verbose_name='client id'
    )
    gender = models.CharField(
        max_length=4, default="Mr",
        choices=Visitor.GENDER_CHOICES,
        verbose_name='civilité',
    )
    name = models.CharField(
        verbose_name="nom & prénoms",
        max_length=100
    )
    phone_one = PhoneNumberField(
        verbose_name="téléphone",
        unique=True
    )
    phone_two = PhoneNumberField(
        verbose_name='second téléphone (facultatif)',
        blank=True, null=True
    )
    faculte = models.CharField(
        verbose_name="faculté",
        max_length=180,
        blank=True, null=True
    )
    amount = models.PositiveIntegerField(
        verbose_name="montant versé (Fr CFA)",
        default=5000,
        validators=[
            MinValueValidator(5000),
            MaxValueValidator(800000)
        ],
        null=True
    )
    number_kit = models.CharField(
        verbose_name="numéro du kit",
        max_length=6,
        default='MKB001', null=True
    )
    is_pack_easy = models.BooleanField(
        verbose_name="easy",
        default=False
    )
    is_pack_gold = models.BooleanField(
        verbose_name="gold",
        default=False
    )
    is_pack_fun = models.BooleanField(
        verbose_name="fun",
        default=False
    )
    is_pack_phoenix = models.BooleanField(
        verbose_name="phoenix",
        default=False
    )
    is_pack_silver = models.BooleanField(
        verbose_name="silver",
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name="date d'ajout",
        auto_now=False,
        auto_now_add=True
    )    

    class Meta:
        db_table = 'db_suscribers'
        ordering = ('-created_at',)
        verbose_name_plural = 'Souscripteurs'
        indexes = [
            models.Index(
                fields=['id', 'uuid'],
                name='id_suscribers'
            ),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "souscriber_detail", kwargs={"pk": self.pk}
        )

    def get_update_url(self):
        return reverse(
            "max:max_update_path", kwargs={"pk": self.pk}
        )
    
    @admin.display(description="client name")
    def get_client_name(self):
        return f"{self.get_gender_display()} {self.name}"
    
    @admin.display(description="téléphone client")
    def get_client_phone(self):
        return self.phone_one

    @admin.display(description='montant versé')
    def get_client_amount(self):
        return self.amount
