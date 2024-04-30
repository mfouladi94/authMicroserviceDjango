from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    
    email = models.EmailField(_('email address'), unique=True)

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    birthdate = models.DateField(_("birth date"), default=timezone.now)
    mobile_number = models.BigIntegerField(_('mobile number'), null=True, blank=True)
    description = models.CharField(_("description"), max_length=255, blank=True)
    location = models.CharField(_("location"), max_length=255, blank=True)
    
    last_seen = models.DateTimeField(_("last seen"), default=timezone.now)
    is_banned = models.BooleanField(_("banned"), default=False)

    is_vip = models.BooleanField(_("vip"), default=False)
    is_kyc_l1_done = models.BooleanField(_("KYC 1"), default=False)
    is_kyc_l2_done = models.BooleanField(_("KYC 2"), default=False)

    is_premium = models.BooleanField(_("premium"), default=False)

    bio = models.TextField(blank=True)

    rating = models.FloatField(default=0)
    irr_balance = models.FloatField(default=0)
    total_balance = models.FloatField(default=0)
    freeze_balance = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email