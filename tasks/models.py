from django.db import models

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
        on_delete=models.CASCADE,
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


















# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     # tasks

#     def __str__(self):
#         return self.name


# class Task(models.Model):
#     project = models.ForeignKey(
#         "Project",
#         on_delete=models.CASCADE,
#         default=1
#     )
#     assigned_to = models.ManyToManyField(Employee, related_name='tasks')
#     # notun_string = models.CharField(max_length=100, default="")
#     title = models.CharField(max_length=250)
#     description = models.TextField()
#     due_date = models.DateField()
#     is_completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     # details

# # One to One
# # Many to One
# # Many to Many


# class TaskDetail(models.Model):
#     HIGH = 'H'
#     MEDIUM = 'M'
#     LOW = 'L'
#     PRIORITY_OPTIONS = (
#         (HIGH, 'High'),
#         (MEDIUM, 'Medium'),
#         (LOW, 'Low')
#     )
#     task = models.OneToOneField(
#         Task,
#         on_delete=models.CASCADE,
#         related_name='details'
#     )
#     assigned_to = models.CharField(max_length=100)
#     priority = models.CharField(
#         max_length=1, choices=PRIORITY_OPTIONS, default=LOW)

# # Task.objects.get(id=2)
# # select * from task where id = 2
# # ORM


# class Project(models.Model):
#     name = models.CharField(max_length=100)
#     start_date = models.DateField()

# task = onekgula employee ekta task
# employee = onekgula task er jonno assign ase


#-----------------eventsfor----------------------
# from django.core.validators import MinLengthValidator, EmailValidator
# from django.utils import timezone

# class Category(models.Model):
#     name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "Categories"


# class Event(models.Model):
#     name = models.CharField(max_length=200, validators=[MinLengthValidator(2)])
#     description = models.TextField()
#     date = models.DateField()
#     time = models.TimeField()
#     location = models.CharField(max_length=200)
#     category = models.ForeignKey(
#         Category, 
#         on_delete=models.SET_NULL, 
#         null=True, 
#         related_name='events'
#     )

#     def __str__(self):
#         return f"{self.name} - {self.date}"

#     @property
#     def is_upcoming(self):
#         today = timezone.now().date()
#         return self.date >= today

#     @property
#     def is_past(self):
#         today = timezone.now().date()
#         return self.date < today


# class Participant(models.Model):
#     name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
#     email = models.EmailField(
#         max_length=100, 
#         unique=True,
#         validators=[EmailValidator()]
#     )
#     events = models.ManyToManyField(Event, related_name='participants', blank=True)

#     def __str__(self):
#         return f"{self.name} ({self.email})"