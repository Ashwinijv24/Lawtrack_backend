import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lawtrack.settings')
django.setup()

from django.utils import timezone
from datetime import timedelta
from accounts.models import User
from cases.models import Client, Case
from events.models import Event
from income.models import Payment

# Create sample users
print('Creating sample users...')
user1, created = User.objects.get_or_create(
    username='john_lawyer',
    defaults={
        'email': 'john@lawfirm.com',
        'first_name': 'John',
        'last_name': 'Smith',
        'role': 'lawyer',
        'is_staff': False
    }
)
if created:
    user1.set_password('password123')
    user1.save()
    print('Created user: john_lawyer')

user2, created = User.objects.get_or_create(
    username='jane_assistant',
    defaults={
        'email': 'jane@lawfirm.com',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'role': 'assistant',
        'is_staff': False
    }
)
if created:
    user2.set_password('password123')
    user2.save()
    print('Created user: jane_assistant')

# Create sample clients
print('Creating sample clients...')
client1, created = Client.objects.get_or_create(
    name='Alice Johnson',
    defaults={
        'phone': '555-0101',
        'email': 'alice@example.com'
    }
)
if created:
    print('Created client: Alice Johnson')

client2, created = Client.objects.get_or_create(
    name='Bob Williams',
    defaults={
        'phone': '555-0102',
        'email': 'bob@example.com'
    }
)
if created:
    print('Created client: Bob Williams')

client3, created = Client.objects.get_or_create(
    name='Carol Davis',
    defaults={
        'phone': '555-0103',
        'email': 'carol@example.com'
    }
)
if created:
    print('Created client: Carol Davis')

# Create sample cases
print('Creating sample cases...')
case1, created = Case.objects.get_or_create(
    title='Smith v. Johnson',
    defaults={
        'description': 'Civil dispute regarding property boundary',
        'status': 'Open',
        'client': client1
    }
)
if created:
    print('Created case: Smith v. Johnson')

case2, created = Case.objects.get_or_create(
    title='Williams Estate Settlement',
    defaults={
        'description': 'Estate planning and settlement case',
        'status': 'In Progress',
        'client': client2
    }
)
if created:
    print('Created case: Williams Estate Settlement')

case3, created = Case.objects.get_or_create(
    title='Davis Contract Dispute',
    defaults={
        'description': 'Commercial contract breach case',
        'status': 'Closed',
        'client': client3
    }
)
if created:
    print('Created case: Davis Contract Dispute')

# Create sample events
print('Creating sample events...')
now = timezone.now()

event1, created = Event.objects.get_or_create(
    title='Court Hearing - Smith v. Johnson',
    case=case1,
    defaults={
        'event_type': 'hearing',
        'date': now + timedelta(days=7),
        'location': 'City Court, Room 101',
        'description': 'Initial hearing for property dispute'
    }
)
if created:
    print('Created event: Court Hearing - Smith v. Johnson')

event2, created = Event.objects.get_or_create(
    title='Client Meeting - Williams Estate',
    case=case2,
    defaults={
        'event_type': 'meeting',
        'date': now + timedelta(days=3),
        'location': 'Law Office, Conference Room A',
        'description': 'Discuss estate distribution'
    }
)
if created:
    print('Created event: Client Meeting - Williams Estate')

event3, created = Event.objects.get_or_create(
    title='Filing Deadline - Davis Contract',
    case=case3,
    defaults={
        'event_type': 'deadline',
        'date': now + timedelta(days=14),
        'location': 'Court Filing Office',
        'description': 'Final document submission deadline'
    }
)
if created:
    print('Created event: Filing Deadline - Davis Contract')

# Create sample payments
print('Creating sample payments...')
payment1, created = Payment.objects.get_or_create(
    case=case1,
    amount=5000.00,
    defaults={
        'status': 'paid',
        'due_date': now.date() - timedelta(days=30),
        'payment_date': now.date() - timedelta(days=25),
        'description': 'Initial consultation and case preparation'
    }
)
if created:
    print('Created payment: $5000 for Smith v. Johnson')

payment2, created = Payment.objects.get_or_create(
    case=case2,
    amount=7500.00,
    defaults={
        'status': 'pending',
        'due_date': now.date() + timedelta(days=15),
        'description': 'Estate planning services'
    }
)
if created:
    print('Created payment: $7500 for Williams Estate Settlement')

payment3, created = Payment.objects.get_or_create(
    case=case3,
    amount=3000.00,
    defaults={
        'status': 'overdue',
        'due_date': now.date() - timedelta(days=10),
        'description': 'Contract review and analysis'
    }
)
if created:
    print('Created payment: $3000 for Davis Contract Dispute')

print('Successfully populated database with sample data!')
