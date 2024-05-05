from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.permissions import IsAdminUser
from .permissions import *
        
class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class SkillClassViewSet(ModelViewSet):
    queryset = SkillClass.objects.all()
    serializer_class = SkillClassSerializer
    permission_classes = [IsTutorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(tutor=self.request.user)

class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsStudent]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsStundetOrReviewOwner]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)