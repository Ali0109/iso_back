from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models, helpers


@receiver(post_save, sender=models.Violation)
def violation_post_save(sender, instance, created, **kwargs):
    if created:
        # multiple_push_notification all registration_id in device model
        helpers.device_helper.multiple_push_notification(
            title="Найдено новое несоответствие",
            body="Нажмите чтобы посмотреть",
        )
    else:
        if instance.status.pk == 2:
            helpers.violation_helper.send_bot_violation_message(instance=instance)
        if instance.status.pk == 3:
            # multiple_push_notification all registration_id in device model
            helpers.device_helper.multiple_push_notification(
                title="Ответственный отдел ответил на несоответсвие",
                body="Нажмите чтобы посмотреть",
            )
