
from django.urls import path
from . import views

urlpatterns = [
    path('', views.income, name='income'),
    path('add/', views.add_payment, name='add_payment'),
    path('<int:payment_id>/', views.payment_detail, name='payment_detail'),
    path('report/', views.financial_report, name='financial_report'),
]
