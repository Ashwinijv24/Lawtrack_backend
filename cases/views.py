
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Client, Case

@login_required
def case_list(request):
    cases = Case.objects.all()
    return render(request, 'cases.html', {'cases': cases})

@login_required
def add_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        client = Client.objects.create(name=name, phone=phone, email=email)
        messages.success(request, f'Client {name} added successfully!')
        return redirect('clients')
    return render(request, 'add_client.html')

@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

@login_required
def create_case(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status', 'Open')
        client_id = request.POST.get('client')
        
        client = get_object_or_404(Client, id=client_id)
        case = Case.objects.create(title=title, description=description, status=status, client=client)
        messages.success(request, f'Case "{title}" created successfully!')
        return redirect('cases')
    
    clients = Client.objects.all()
    return render(request, 'create_case.html', {'clients': clients})

@login_required
def case_detail(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    return render(request, 'case_detail.html', {'case': case})

@login_required
def update_case_status(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    if request.method == 'POST':
        case.status = request.POST.get('status')
        case.save()
        messages.success(request, 'Case status updated successfully!')
        return redirect('case_detail', case_id=case_id)
    return redirect('case_detail', case_id=case_id)
