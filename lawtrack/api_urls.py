from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.api_views import RegisterView, LoginView, MeView
from cases.api_views import ClientViewSet, CaseViewSet
from documents.api_views import DocumentViewSet
from events.api_views import EventViewSet
from income.api_views import PaymentViewSet

router = DefaultRouter()
router.register('clients', ClientViewSet)
router.register('cases', CaseViewSet)
router.register('documents', DocumentViewSet)
router.register('events', EventViewSet)
router.register('payments', PaymentViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('auth/me/', MeView.as_view()),
    path('', include(router.urls)),
]
