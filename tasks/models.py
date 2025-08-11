from django.db import models
from django.db.models.signals import post_save, pre_save, m2m_changed, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name



class Event(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed')
    ]
    Category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        default=1
    )
    assigned_to = models.ManyToManyField(Participant, related_name='Events')
    assigned_to = models.ManyToManyField(Participant)
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="PENDING")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class EventDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    )

    event = models.OneToOneField(
        Event,
        on_delete=models.DO_NOTHING,
        #models.CASCADE,
        related_name='details'
    )
    priority = models.CharField(
        max_length=1, choices=PRIORITY_OPTIONS, default=LOW)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Details form Event {self.event.title}"




class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"





#signals
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