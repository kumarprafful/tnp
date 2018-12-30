import random, string
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class UserManager(BaseUserManager):

    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Provide your email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

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
        print("X", x)
        y = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        print("Y", y)
        z = x+y
        print("ENR", z)
        return z

class StudentProfile(models.Model):
    class Meta:
        verbose_name = "Student Profile"

    COLLEGE = (
        ('USICT', 'U.S.I.C.T.'),
    )

    COURSE = (
        ('BtechCSE', 'B.TECH - CSE'),
        ('BtechIT', 'B.TECH - IT'),
        ('BtechECE', 'B.TECH - ECE'),
        ('MtechCSE', 'M.TECH - CSE'),
        ('MtechIT', 'M.TECH - IT'),
        ('MtechECE', 'M.TECH - ECE'),
        ('MCA', 'MCA'),
    )

    YEAR_CHOICES = []
    for r in range(2015, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    REGION = (
        ('DEL', 'Delhi'),
        ('ODEL', 'Outside Delhi'),
    )

    CATEGORY = (
        ('UR', 'Unreserved'),
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OTH', 'Other'),
    )



    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    enrollment_no = models.CharField(max_length=20, unique=True, null=False, blank=False)
    name = models.CharField(_("Full Name"), max_length=100, blank=True, null=True)
    college = models.CharField(max_length=10,choices=COLLEGE,default='USICT')
    course = models.CharField(max_length = 20, choices=COURSE, blank=True, null=True)
    dob = models.DateField(_("Date of birth"), blank=True, null=True)
    admission_year = models.IntegerField(_('Year of Admission'), choices=YEAR_CHOICES, blank=True, null=True)
    fathers_name = models.CharField(max_length=50, null=True, blank=True)
    region = models.CharField(max_length=20, choices=REGION, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, blank=True, null=True)
    mobile = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(9999999999)])



    def __str__(self):
        return self.user.email

class FacultyProfile(models.Model):
    class Meta:
        verbose_name = 'Faculty Profile'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



    def __str__(self):
        return self.user.email
