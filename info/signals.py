from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import Campaign

@receiver(pre_save, sender=Campaign)
def remove_expired_campaign(sender, instance, **kwargs):
    # Check if the end date has passed
    if instance.end_date < timezone.now():
        # End date has passed, remove the campaign
        instance.delete()