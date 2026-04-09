import os
import django
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lawtrack.settings')
django.setup()

from django.utils import timezone
from datetime import timedelta
from cases.models import Case
from documents.models import Document

print('Adding sample documents...\n')

# Get all cases
cases = Case.objects.all()

if not cases.exists():
    print('No cases found. Please run populate_data.py first.')
    exit()

# Sample documents data
documents_data = [
    ('Case_Brief_Smith_v_Johnson.pdf', 'pdf', 'Case brief and legal analysis', 'Smith v. Johnson'),
    ('Property_Deed_Miller.pdf', 'pdf', 'Original property deed document', 'Miller Property Rights'),
    ('Employment_Contract_Wilson.pdf', 'pdf', 'Employment contract and terms', 'Wilson Employment Case'),
    ('Divorce_Agreement_Taylor.pdf', 'pdf', 'Divorce settlement agreement', 'Taylor Divorce Settlement'),
    ('Merger_Agreement_Anderson.pdf', 'pdf', 'Business merger agreement', 'Anderson Business Merger'),
    ('Patent_Application_Thomas.pdf', 'pdf', 'Patent application documents', 'Thomas Intellectual Property'),
    ('Insurance_Claim_Jackson.pdf', 'pdf', 'Insurance claim documentation', 'Jackson Insurance Claim'),
    ('Medical_Records_White.pdf', 'pdf', 'Medical records and reports', 'White Medical Malpractice'),
    ('Evidence_Photo_1.jpg', 'image', 'Crime scene photograph', 'Brown v. State'),
    ('Evidence_Photo_2.jpg', 'image', 'Property damage photograph', 'Miller Property Rights'),
    ('Deposition_Video_Wilson.mp4', 'video', 'Witness deposition video', 'Wilson Employment Case'),
    ('Court_Hearing_Recording.mp4', 'video', 'Court hearing recording', 'Taylor Divorce Settlement'),
    ('Expert_Report_Anderson.pdf', 'pdf', 'Expert witness report', 'Anderson Business Merger'),
    ('Technical_Analysis_Thomas.pdf', 'pdf', 'Technical patent analysis', 'Thomas Intellectual Property'),
    ('Damage_Assessment_Jackson.pdf', 'pdf', 'Property damage assessment', 'Jackson Insurance Claim'),
    ('Medical_Expert_Report_White.pdf', 'pdf', 'Medical expert opinion', 'White Medical Malpractice'),
    ('Witness_Statement_Brown.pdf', 'pdf', 'Witness statement document', 'Brown v. State'),
    ('Survey_Report_Miller.pdf', 'pdf', 'Property survey report', 'Miller Property Rights'),
    ('Email_Evidence_Wilson.pdf', 'pdf', 'Email correspondence evidence', 'Wilson Employment Case'),
    ('Settlement_Proposal_Taylor.pdf', 'pdf', 'Settlement proposal document', 'Taylor Divorce Settlement'),
]

print('Creating sample documents...')
created_count = 0

for filename, doc_type, description, case_title in documents_data:
    # Find the case
    try:
        case = Case.objects.get(title=case_title)
    except Case.DoesNotExist:
        print(f'  ⚠️  Case not found: {case_title}')
        continue
    
    # Create document
    document, created = Document.objects.get_or_create(
        title=filename.replace('_', ' ').replace('.pdf', '').replace('.jpg', '').replace('.mp4', ''),
        case=case,
        defaults={
            'document_type': doc_type,
            'description': description,
            'file': ContentFile(b'Sample document content', name=filename)
        }
    )
    
    if created:
        print(f'  ✅ Created document: {filename} ({doc_type}) for {case_title}')
        created_count += 1
    else:
        print(f'  ℹ️  Document already exists: {filename}')

print(f'\n✅ Successfully added {created_count} sample documents!')
print(f'Total Documents: {Document.objects.count()}')

# Print summary by type
print('\nDocuments by Type:')
print(f'  📄 PDFs: {Document.objects.filter(document_type="pdf").count()}')
print(f'  🖼️  Images: {Document.objects.filter(document_type="image").count()}')
print(f'  🎥 Videos: {Document.objects.filter(document_type="video").count()}')
print(f'  📎 Other: {Document.objects.filter(document_type="other").count()}')

print('\nDocuments by Case:')
for case in cases:
    doc_count = case.documents.count()
    if doc_count > 0:
        print(f'  {case.title}: {doc_count} documents')
