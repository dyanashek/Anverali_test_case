from django.db import models
from django.contrib.auth.models import AbstractUser
from core.validators.validators import validate_phone_number
from core.choices.choices import GENDER, CURRENCY


class CustomUser(AbstractUser):
    sex = models.CharField(
        max_length=6,
        choices=GENDER,
        blank=True,
        verbose_name='Gender',
    )
    phone = models.CharField(
        max_length=20,
        help_text='Required. Digits and + only, no longer then 20 symbols and shorter then 6 symbols.',
        validators=[validate_phone_number,],
        verbose_name='Phone number',
    )
    role = models.CharField(
        max_length=20,
        default='admin',
        blank=True,
        verbose_name='Role',
    )


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='customer_profile', 
        default=None, 
        null=True,
        )
    currency = models.CharField(
        max_length=7,
        choices=CURRENCY,
        blank=True,
        verbose_name='Settlement currency'
    )


class FreelancerProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='freelancer_profile', 
        default=None, 
        null=True,
        )
    specialization = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Specialization'
    )