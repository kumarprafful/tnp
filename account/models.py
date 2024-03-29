import random, string
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
import datetime

# Create your models here.
class UserManager(BaseUserManager):

    def _create_user(self, email, password, enrollment_no=None, **kwargs):
        if not email:
            raise ValueError("Provide your email address")
        email = self.normalize_email(email)
        if enrollment_no is not None:
            user = self.model(email=email,enrollment_no=enrollment_no, **kwargs)
        if enrollment_no is None:
            user = self.model(email=email, **kwargs)
            user.enrollment_no = user.fill_enr_no()
            user.is_faculty = True
            user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, enrollment_no=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, enrollment_no, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must be a staffself.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must be a superuser')
        return self._create_user(email, password, **kwargs)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    enrollment_no = models.CharField(max_length=20, unique=True, null=False, blank=False)
    is_faculty = models.BooleanField(default=False, help_text="Designates whether the account is of student's or faculty")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def fill_enr_no(self):
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        y = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        z = x+y
        return z



class FacultyProfile(models.Model):
    class Meta:
        verbose_name = 'Faculty Profile'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



    def __str__(self):
        return self.user.email
