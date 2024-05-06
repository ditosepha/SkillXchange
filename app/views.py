from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.permissions import IsAdminUser
from .permissions import *
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
        
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

        skill_class = serializer.validated_data['skill_class']
        enrolled_students_count = skill_class.enrollments.count()
        if enrolled_students_count >= skill_class.max_students:
            raise ValidationError({"error": "Maximum number of students already enrolled in this class."})
        serializer.save(student=self.request.user)

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsStundetOrReviewOwner]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)