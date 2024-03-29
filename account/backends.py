from student.models import StudentProfile
from django.db.models import Q
from django.conf import settings

from .models import User

class EnrollmentBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(Q(enrollment_no=username) |Q(email=username))
        except User.DoesNotExist:
            return None
        return user if user.check_password(password) else None
