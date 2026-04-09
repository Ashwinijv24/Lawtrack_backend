from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(detail=False, methods=['get'])
    def report(self, request):
        payments = Payment.objects.all()
        return Response({
            'total': payments.filter(status='paid').aggregate(Sum('amount'))['amount__sum'] or 0,
            'pending': payments.filter(status='pending').aggregate(Sum('amount'))['amount__sum'] or 0,
            'overdue': payments.filter(status='overdue').aggregate(Sum('amount'))['amount__sum'] or 0,
        })
