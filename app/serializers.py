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
    
    def update(self, instance, validated_data):
        # Prevent tutors from changing the tutor field
        if 'tutor' in validated_data:
            existing_tutor = instance.tutor
            new_tutor_id = validated_data['tutor'].id if validated_data['tutor'] else None
            if existing_tutor.id != new_tutor_id:
                raise serializers.ValidationError("Tutors are not allowed to change the tutor field.")
        return super().update(instance, validated_data)

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"

    def update(self, instance, validated_data):
        # Prevent students from changing the student field
        if 'student' in validated_data:
            existing_student = instance.student
            new_student_id = validated_data['student'].id if validated_data['student'] else None
            if existing_student.id != new_student_id:
                raise serializers.ValidationError("Student are not allowed to change the student field.")
        return super().update(instance, validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
    
    def update(self, instance, validated_data):
        # Prevent students from changing the student field
        if 'student' in validated_data:
            existing_student = instance.student
            new_student_id = validated_data['student'].id if validated_data['student'] else None
            if existing_student.id != new_student_id:
                raise serializers.ValidationError("Student are not allowed to change the student field.")
        return super().update(instance, validated_data)