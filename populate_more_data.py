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

print('Adding more sample data...\n')

# Create more clients
print('Creating additional clients...')
clients_data = [
    ('Michael Brown', '555-0104', 'michael@example.com'),
    ('Sarah Miller', '555-0105', 'sarah@example.com'),
    ('David Wilson', '555-0106', 'david@example.com'),
    ('Emma Taylor', '555-0107', 'emma@example.com'),
    ('James Anderson', '555-0108', 'james@example.com'),
    ('Lisa Thomas', '555-0109', 'lisa@example.com'),
    ('Robert Jackson', '555-0110', 'robert@example.com'),
    ('Jennifer White', '555-0111', 'jennifer@example.com'),
]

clients = []
for name, phone, email in clients_data:
    client, created = Client.objects.get_or_create(
        name=name,
        defaults={'phone': phone, 'email': email}
    )
    clients.append(client)
    if created:
        print(f'  Created client: {name}')

# Create more cases
print('\nCreating additional cases...')
cases_data = [
    ('Brown v. State', 'Criminal defense case', 'Open', clients[0]),
    ('Miller Property Rights', 'Real estate dispute', 'In Progress', clients[1]),
    ('Wilson Employment Case', 'Wrongful termination lawsuit', 'Open', clients[2]),
    ('Taylor Divorce Settlement', 'Family law case', 'In Progress', clients[3]),
    ('Anderson Business Merger', 'Corporate law matter', 'Closed', clients[4]),
    ('Thomas Intellectual Property', 'Patent infringement case', 'Open', clients[5]),
    ('Jackson Insurance Claim', 'Insurance dispute', 'In Progress', clients[6]),
    ('White Medical Malpractice', 'Medical negligence case', 'Open', clients[7]),
]

cases = []
for title, description, status, client in cases_data:
    case, created = Case.objects.get_or_create(
        title=title,
        defaults={
            'description': description,
            'status': status,
            'client': client
        }
    )
    cases.append(case)
    if created:
        print(f'  Created case: {title}')

# Create more events
print('\nCreating additional events...')
now = timezone.now()

events_data = [
    ('Deposition - Brown v. State', 'hearing', now + timedelta(days=5), 'District Court, Room 205', 'Witness deposition'),
    ('Client Consultation - Miller', 'meeting', now + timedelta(days=2), 'Law Office, Room 301', 'Discuss property boundaries'),
    ('Motion Hearing - Wilson', 'hearing', now + timedelta(days=10), 'Superior Court, Room 102', 'Motion for summary judgment'),
    ('Settlement Conference - Taylor', 'meeting', now + timedelta(days=4), 'Mediation Center', 'Divorce settlement negotiation'),
    ('Board Meeting - Anderson', 'meeting', now + timedelta(days=1), 'Corporate Office', 'Merger approval meeting'),
    ('Patent Office Hearing - Thomas', 'hearing', now + timedelta(days=20), 'Patent Office, DC', 'Patent infringement hearing'),
    ('Insurance Adjuster Meeting - Jackson', 'meeting', now + timedelta(days=3), 'Insurance Office', 'Claim review meeting'),
    ('Expert Witness Deposition - White', 'hearing', now + timedelta(days=8), 'Medical Center', 'Medical expert testimony'),
    ('Document Review Deadline - Brown', 'deadline', now + timedelta(days=6), 'Law Office', 'Complete document discovery'),
    ('Filing Deadline - Miller', 'deadline', now + timedelta(days=12), 'Court Filing Office', 'File amended complaint'),
]

for title, event_type, date, location, description in events_data:
    # Find a case that matches the event
    case = None
    for c in cases:
        if c.title.split()[0].lower() in title.lower():
            case = c
            break
    if case is None:
        case = cases[0]
    
    event, created = Event.objects.get_or_create(
        title=title,
        case=case,
        defaults={
            'event_type': event_type,
            'date': date,
            'location': location,
            'description': description
        }
    )
    if created:
        print(f'  Created event: {title}')

# Create more payments
print('\nCreating additional payments...')
payments_data = [
    (cases[0], 8000.00, 'paid', now.date() - timedelta(days=45), now.date() - timedelta(days=40), 'Criminal defense retainer'),
    (cases[1], 6500.00, 'pending', now.date() + timedelta(days=20), None, 'Property survey and analysis'),
    (cases[2], 9500.00, 'overdue', now.date() - timedelta(days=15), None, 'Employment law consultation'),
    (cases[3], 5500.00, 'paid', now.date() - timedelta(days=60), now.date() - timedelta(days=55), 'Divorce mediation services'),
    (cases[4], 12000.00, 'paid', now.date() - timedelta(days=90), now.date() - timedelta(days=85), 'Corporate merger review'),
    (cases[5], 10500.00, 'pending', now.date() + timedelta(days=30), None, 'Patent prosecution services'),
    (cases[6], 4500.00, 'overdue', now.date() - timedelta(days=20), None, 'Insurance claim investigation'),
    (cases[7], 11000.00, 'pending', now.date() + timedelta(days=25), None, 'Medical malpractice litigation'),
    (cases[0], 3500.00, 'paid', now.date() - timedelta(days=20), now.date() - timedelta(days=15), 'Additional legal research'),
    (cases[1], 2800.00, 'pending', now.date() + timedelta(days=10), None, 'Title search and review'),
]

for case, amount, status, due_date, payment_date, description in payments_data:
    payment, created = Payment.objects.get_or_create(
        case=case,
        amount=amount,
        due_date=due_date,
        defaults={
            'status': status,
            'payment_date': payment_date,
            'description': description
        }
    )
    if created:
        print(f'  Created payment: ${amount} for {case.title}')

print('\n✅ Successfully added more sample data to the database!')
print(f'\nTotal Clients: {Client.objects.count()}')
print(f'Total Cases: {Case.objects.count()}')
print(f'Total Events: {Event.objects.count()}')
print(f'Total Payments: {Payment.objects.count()}')
