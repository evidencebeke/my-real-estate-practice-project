from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel


# Create your models here.
class Enquiry(TimeStampedUUIDModel):
    name = models.CharField(verbose_name=_("Your name"), max_length=100)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone number"), max_length=30, default="+23481862329"
    )
    email = models.EmailField(verbose_name=_("Email"), default="ijobra20@gmail.com")
    subject = models.CharField(verbose_name=_("Subkect"), max_length=100)
    message = models.TextField(verbose_name=_("Your message"))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"
