from django.db.models.signals import post_save, pre_save, m2m_changed, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from tasks.models import Event

@receiver(m2m_changed, sender=Event)

def notify_participant_on_event_creation(sender, instance, action, **kwargs):
    if action == 'post_add':
        print(instance, instance.assigned_to.all())

        assigned_emails = [pats.email for pats in instance.assigned_to.all()]
        print("checking..., assigned_emails")
        send_mail(
            'New Events Assigned',
            f'You have been assigned to the event: {instance.title}',
            'taiyebaafrin32@gmail.com',
            assigned_emails,
            fail_silently=False,
            )






@receiver(post_delete, sender=Event)
def delete_associate_details(sender, instance, **kwargs):
    if instance.details:
        print(isinstance)
        instance.details.delete()
        print('deleted successfully')