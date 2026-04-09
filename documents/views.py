
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Document
from cases.models import Case

@login_required
def documents(request):
    documents = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'documents.html', {'documents': documents})

@login_required
def upload_document(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        case_id = request.POST.get('case')
        document_type = request.POST.get('document_type')
        description = request.POST.get('description', '')
        file = request.FILES.get('file')
        
        case = get_object_or_404(Case, id=case_id)
        document = Document.objects.create(
            title=title,
            case=case,
            document_type=document_type,
            description=description,
            file=file
        )
        messages.success(request, f'Document "{title}" uploaded successfully!')
        return redirect('documents')
    
    cases = Case.objects.all()
    return render(request, 'upload_document.html', {'cases': cases})

@login_required
def document_detail(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    return render(request, 'document_detail.html', {'document': document})

@login_required
def case_documents(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    documents = case.documents.all()
    return render(request, 'case_documents.html', {'case': case, 'documents': documents})
