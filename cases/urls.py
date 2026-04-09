
from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_list, name='cases'),
    path('create/', views.create_case, name='create_case'),
    path('<int:case_id>/', views.case_detail, name='case_detail'),
    path('<int:case_id>/update-status/', views.update_case_status, name='update_case_status'),
    path('clients/', views.client_list, name='clients'),
    path('clients/add/', views.add_client, name='add_client'),
]
