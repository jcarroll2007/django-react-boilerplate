from django.db import models
from django.conf import settings

class StringList(models.Model):
    value = models.CharField(max_length=250, blank=False)

    class Meta:
        abstract = True

class ExcitedAbout(StringList):
    pass

#TODO: Determine read only fields
class DailySummary(models.Model):
    affirmation = models.CharField(max_length=100, blank=True, default='')
    excited_about = models.ManyToManyField(
        ExcitedAbout,
        related_name='excited_about',
        blank=True,
    )
    created = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    date = models.DateField(null=False, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        unique_for_date='date',
        null=False
    )
