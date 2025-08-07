import os
import django
from faker import Faker
import random
from tasks.models import Event, EventDetail, Participant, Category
from django.utils import timezone

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

def populate_db():
    # Initialize Faker
    fake = Faker()

    # Create Categories
    categories = [Category.objects.create(
        name=fake.bs().capitalize(),
        description=fake.paragraph(),
        start_date=fake.date_this_year()
    ) for _ in range(5)]
    print(f"Created {len(categories)} categories.")

    # Create Participants
    participants = [Participant.objects.create(
        name=fake.name(),
        email=fake.email()
    ) for _ in range(10)]
    print(f"Created {len(participants)} participants.")

    # Create Events - USING CORRECT FIELD NAMES
    events = []
    for _ in range(20):
        event = Event.objects.create(
            category=random.choice(categories),
            title=fake.sentence(),
            description=fake.paragraph(),
            due_date=fake.date_this_year(),
            status=random.choice(['PENDING', 'IN_PROGRESS', 'COMPLETED']),
            is_completed=random.choice([True, False])
        )
        # Assign random participants
        event.assigned_to.set(random.sample(participants, random.randint(1, 3)))
        events.append(event)
    print(f"Created {len(events)} events.")

    # Create Event Details
    for event in events:
        EventDetail.objects.create(
            event=event,
            assigned_to=", ".join([participant.name for participant in event.assigned_to.all()]),
            priority=random.choice(['H', 'M', 'L']),
            notes=fake.paragraph()
        )
    print("Populated EventDetails for all events.")
    print("Database populated successfully!")

if __name__ == '__main__':
    print("Starting database population...")
    populate_db()