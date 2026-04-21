from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Document, AuditLog

@receiver(post_save, sender=Document)
def log_document_activity(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'

    AuditLog.objects.create(
        action=action,
        model_name='Document',
        object_id=instance.id,
        actor=instance.created_by
    )