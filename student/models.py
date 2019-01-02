from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime

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
    for r in range(2015, (datetime.now().year+1)):
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
    tweth_marks = models.IntegerField(_("12th marks"), blank=True, null=True)
    mobile = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(9999999999)])



    def __str__(self):
        return self.user.email


class MarkSheet(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    semester_1 = models.IntegerField(blank=True, null=True)
    semester_2 = models.IntegerField(blank=True, null=True)
    semester_3 = models.IntegerField(blank=True, null=True)
    semester_4 = models.IntegerField(blank=True, null=True)
    semester_5 = models.IntegerField(blank=True, null=True)
    semester_6 = models.IntegerField(blank=True, null=True)
    semester_7 = models.IntegerField(blank=True, null=True)
    semester_8 = models.IntegerField(blank=True, null=True)
    CGPA = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.student.user
