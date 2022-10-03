from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel

# Create your models here.
User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+2349343949394"
    )
    about_me = models.TextField(
        verbose_name=_("About Me"), default=_("Say something about you")
    )
    lincense = models.CharField(
        max_length=20, verbose_name=_("Real Estate lincense"), blank=True, null=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile photo"), default="/default.png"
    )
    gender = models.CharField(
        choices=Gender.choices,
        verbose_name=_("Gender"),
        default=Gender.MALE,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("Country"), default="NG", blank=False, null=False
    )
    city = models.CharField(max_length=50, verbose_name=_("City"), default="Lagos")
    is_buyer = models.BooleanField(
        verbose_name=_("Buyer"),
        default=False,
        help_text="Are you looking to buy Property?",
    )
    is_seller = models.BooleanField(
        verbose_name=_("Seller"), default=False, help_text="Are you an agent?"
    )
    is_agent = models.BooleanField(
        verbose_name=_("Agent"),
        default=False,
        help_text="Are you looking to buy Property",
    )
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(
        verbose_name=_("Number of reviews"), null=True, blank=True, default=0
    )

    def __str__(self) -> str:
        return f"{ self.user.username}'s profile"
