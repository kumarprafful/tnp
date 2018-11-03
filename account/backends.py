from account.models import StudentProfile
from django.db.models import Q
from django.conf import settings

class EnrollmentBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False
    print("ATLEAST THIS IS BEING CALLED")

    def get_user(self, user_id):
        print("USER CALLING CALLING USER")
        try:
            return StudentProfile.objects.get(pk=user_id)
        except StudentProfile.DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None):
        print("calling")
        try:
            user = StudentProfile.objects.get(
                Q(enrollment_no=username)
            )
        except StudentProfile.DoesNotExist:
            return None
        return user if user.user.check_password(password) else None
