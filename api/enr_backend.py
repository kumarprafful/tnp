from rest_framework import authentication

class DrfAuthBackend(authentication.BaseAuthentication):
    def authenticate(self, username=None, password=None):
        print("LLLLLLLLLLLLL")

        try:
            user = get_user_model().objects.get(email=username)
            print("HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

            if user.check_password(password):
                return user, None
        except User.DoesNotExist:
            print("NOOOOOOOOOOOOOOOOOOOOO")
            if username.isdigit():
                try:
                    user=get_user_model().objects.get(enrollment_no=username)
                    if user.check_password(password):
                        return user, None
                except User.DoesNotExist:
                    return None
            else:
                return None
