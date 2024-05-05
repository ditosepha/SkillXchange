from rest_framework.permissions import BasePermission

class IsTutorOrReadOnly(BasePermission):
    """
    Custom permission to allow only tutors to add Skill classes,
    and only owners of the classes to edit or delete them.
    """
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.role == 'tutor'
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.tutor == request.user
        return True

class IsStundetOrReviewOwner(BasePermission):
    """
    Custom permission to allow only stundets to add reviews,
    and only owners of the reviews to edit or delete them.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.role == 'student'
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return obj.student == request.user
        return True

class IsStudent(BasePermission):
    """
    Custom permission to allow only students to enroll or un-enroll themselves from classes.
    """

    def has_permission(self, request, view):
        if request.method in ['POST', 'DELETE']:
            return request.user.role == 'student'
        return True