from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import *
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'skillclasses', SkillClassViewSet)
router.register(r'users', UserViewSet)
router.register(r'enrollment', EnrollmentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
