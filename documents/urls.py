
from django.urls import path
from . import views

urlpatterns = [
    path('', views.documents, name='documents'),
    path('upload/', views.upload_document, name='upload_document'),
    path('<int:doc_id>/', views.document_detail, name='document_detail'),
    path('case/<int:case_id>/', views.case_documents, name='case_documents'),
]
