from rest_framework import authentication

class DrfAuthBackend(authentication.BaseAuthentication):
    def authenticate(self, username=None, password=None):

        try:
            user = get_user_model().objects.get(email=username)

            if user.check_password(password):
                return user, None
        except User.DoesNotExist:
            if username.isdigit():
                try:
                    user=get_user_model().objects.get(enrollment_no=username)
                    if user.check_password(password):
                        return user, None
                except User.DoesNotExist:
                    return None
            else:
                return None
