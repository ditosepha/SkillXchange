from rest_framework import serializers
from .models import SkillClass, Enrollment, Review, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'is_superuser', "role", ]

class SkillClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillClass
        fields = "__all__"

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
        
    def validate(self, data):
        existing_enrollments = Enrollment.objects.filter(student=data['student'], skill_class=data['skill_class'])
        if existing_enrollments.exists():
            raise serializers.ValidationError("Student is already enrolled in this SkillClass")
        return data

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
    
    def validate(self, data):
        existing_review = Review.objects.filter(student=data['student'], review=data['review'])
        if existing_review.exists():
            raise serializers.ValidationError("You have already submitted a review for this class.")
        return data