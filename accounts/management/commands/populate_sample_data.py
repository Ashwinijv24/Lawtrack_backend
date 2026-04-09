from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from accounts.models import User
from cases.models import Client, Case
from events.models import Event
from income.models import Payment

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        # Create sample users
        self.stdout.write('Creating sample users...')
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

        # Create sample clients
        self.stdout.write('Creating sample clients...')
        client1, _ = Client.objects.get_or_create(
            name='Alice Johnson',
            defaults={
                'phone': '555-0101',
                'email': 'alice@example.com'
            }
        )
        
        client2, _ = Client.objects.get_or_create(
            name='Bob Williams',
            defaults={
                'phone': '555-0102',
                'email': 'bob@example.com'
            }
        )
        
        client3, _ = Client.objects.get_or_create(
            name='Carol Davis',
            defaults={
                'phone': '555-0103',
                'email': 'carol@example.com'
            }
        )

        # Create sample cases
        self.stdout.write('Creating sample cases...')
        case1, _ = Case.objects.get_or_create(
            title='Smith v. Johnson',
            defaults={
                'description': 'Civil dispute regarding property boundary',
                'status': 'Open',
                'client': client1
            }
        )
        
        case2, _ = Case.objects.get_or_create(
            title='Williams Estate Settlement',
            defaults={
                'description': 'Estate planning and settlement case',
                'status': 'In Progress',
                'client': client2
            }
        )
        
        case3, _ = Case.objects.get_or_create(
            title='Davis Contract Dispute',
            defaults={
                'description': 'Commercial contract breach case',
                'status': 'Closed',
                'client': client3
            }
        )

        # Create sample events
        self.stdout.write('Creating sample events...')
        now = timezone.now()
        
        Event.objects.get_or_create(
            title='Court Hearing - Smith v. Johnson',
            case=case1,
            defaults={
                'event_type': 'hearing',
                'date': now + timedelta(days=7),
                'location': 'City Court, Room 101',
                'description': 'Initial hearing for property dispute'
            }
        )
        
        Event.objects.get_or_create(
            title='Client Meeting - Williams Estate',
            case=case2,
            defaults={
                'event_type': 'meeting',
                'date': now + timedelta(days=3),
                'location': 'Law Office, Conference Room A',
                'description': 'Discuss estate distribution'
            }
        )
        
        Event.objects.get_or_create(
            title='Filing Deadline - Davis Contract',
            case=case3,
            defaults={
                'event_type': 'deadline',
                'date': now + timedelta(days=14),
                'location': 'Court Filing Office',
                'description': 'Final document submission deadline'
            }
        )

        # Create sample payments
        self.stdout.write('Creating sample payments...')
        Payment.objects.get_or_create(
            case=case1,
            defaults={
                'amount': 5000.00,
                'status': 'paid',
                'due_date': now.date() - timedelta(days=30),
                'payment_date': now.date() - timedelta(days=25),
                'description': 'Initial consultation and case preparation'
            }
        )
        
        Payment.objects.get_or_create(
            case=case2,
            defaults={
                'amount': 7500.00,
                'status': 'pending',
                'due_date': now.date() + timedelta(days=15),
                'description': 'Estate planning services'
            }
        )
        
        Payment.objects.get_or_create(
            case=case3,
            defaults={
                'amount': 3000.00,
                'status': 'overdue',
                'due_date': now.date() - timedelta(days=10),
                'description': 'Contract review and analysis'
            }
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data'))
