from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Letter(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_("Your Email Address"), max_length=254)
    subject = models.CharField(_("Subject"), max_length=50)
    message = models.TextField(_("Message"))
    date_posted = models.DateField(_("Date"), auto_now=True, auto_now_add=False)
