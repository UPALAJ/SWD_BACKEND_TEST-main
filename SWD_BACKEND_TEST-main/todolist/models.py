from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class todolistmodel(models.Model):
    created_date = models.DateField(
        auto_now_add=True,
        verbose_name=_("Created Date")
    )
    updated_date = models.DateField(
        auto_now=True,
        verbose_name=_("Updated Date")
    )
    element = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name=_('Element')
    )