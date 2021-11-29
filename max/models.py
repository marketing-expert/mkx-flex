# max.models.py

import uuid
from django.db import models
from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator

import phonenumbers
from flex.models import Visitor
from phonenumber_field.modelfields import PhoneNumberField


class Pack(models.Model):

    class PACK_TYPES(models.TextChoices):
        FUN = "FUN", "FUN"
        GOLD = "GOLD", "Gold"
        SILVER = "SILVER", "Silver"

    default_pack_choices = PACK_TYPES.FUN

    pack = models.CharField(
        verbose_name="pack",
        max_length=10,
        default=default_pack_choices,
        choices=PACK_TYPES.choices
    )
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
    email = models.EmailField(
        unique=True,
        max_length=254,
        verbose_name='adresse email'
    )
    phone_one = PhoneNumberField(
        verbose_name="téléphone",
        unique=True
    )
    phone_two = PhoneNumberField(
        verbose_name='second téléphone (facultatif)',
        blank=True, null=True
    )
    packs = models.ManyToManyField(
        to=Pack,
        verbose_name="packs",
        related_name="packs"
    )
    faculte = models.CharField(
        verbose_name="faculté",
        max_length=180,
        help_text="faculté du client"
    )
    amount = models.PositiveIntegerField(
        verbose_name="montant versé",
        default=5000
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
    
    @admin.display(description="client name")
    def get_client_name(self):
        return f"{self.get_gender_display()} {self.name}"
    
    def formatted_phone_one(self, country=None):
        return phonenumbers.parse(self.phone_one, country)

    def formatted_phone_two(self, country=None):
        return phonenumbers.parse(self.phone_two, country)
    
    @admin.display(description="téléphone client")
    def get_client_phone(self):
        return self.formatted_phone_one()
    
    @admin.display(description='montant versé')
    def get_client_amount(self):
        return self.amount
    
    @admin.display(description='packs choisis')
    def get_client_packs(self):
        packs = [pack.name for pack in self.packs.all()]
        return packs
