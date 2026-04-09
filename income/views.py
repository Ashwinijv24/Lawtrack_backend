
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Payment
from cases.models import Case

@login_required
def income(request):
    payments = Payment.objects.all()
    total_income = payments.filter(status='paid').aggregate(Sum('amount'))['amount__sum'] or 0
    pending_income = payments.filter(status='pending').aggregate(Sum('amount'))['amount__sum'] or 0
    
    return render(request, 'income.html', {
        'payments': payments,
        'total_income': total_income,
        'pending_income': pending_income
    })

@login_required
def add_payment(request):
    if request.method == 'POST':
        case_id = request.POST.get('case')
        amount = request.POST.get('amount')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        payment_date = request.POST.get('payment_date') or None
        description = request.POST.get('description', '')
        
        case = get_object_or_404(Case, id=case_id)
        payment = Payment.objects.create(
            case=case,
            amount=amount,
            status=status,
            due_date=due_date,
            payment_date=payment_date,
            description=description
        )
        messages.success(request, f'Payment of ${amount} added successfully!')
        return redirect('income')
    
    cases = Case.objects.all()
    return render(request, 'add_payment.html', {'cases': cases})

@login_required
def payment_detail(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    return render(request, 'payment_detail.html', {'payment': payment})

@login_required
def financial_report(request):
    payments = Payment.objects.all()
    total_income = payments.filter(status='paid').aggregate(Sum('amount'))['amount__sum'] or 0
    pending_income = payments.filter(status='pending').aggregate(Sum('amount'))['amount__sum'] or 0
    overdue_income = payments.filter(status='overdue').aggregate(Sum('amount'))['amount__sum'] or 0
    
    paid_payments = payments.filter(status='paid')
    pending_payments = payments.filter(status='pending')
    overdue_payments = payments.filter(status='overdue')
    
    return render(request, 'financial_report.html', {
        'total_income': total_income,
        'pending_income': pending_income,
        'overdue_income': overdue_income,
        'paid_payments': paid_payments,
        'pending_payments': pending_payments,
        'overdue_payments': overdue_payments,
    })
