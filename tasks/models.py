from django.db import models
from django.contrib.auth.models import User



# # Create your models here.
# class Participant(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     def __str__(self):
#         return self.name



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
    #assigned_to = models.ManyToManyField(Participant, related_name='Events')
    assigned_to = models.ManyToManyField(User, related_name='Events')
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="PENDING")
    # is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class EventAssignment(models.Model):
    Participant = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)


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

