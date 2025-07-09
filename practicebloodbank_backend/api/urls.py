from django.urls import path, include
from .views import RegisterView, CustomAuthToken, DonationViewSet, BloodInventoryViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'donations', DonationViewSet, basename='donation')
router.register(r'blood', BloodInventoryViewSet, basename='blood')
router.register(r'users', UserViewSet, basename='user')  # for user viewset access

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # ← this is your registration endpoint
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('', include(router.urls)),
]
