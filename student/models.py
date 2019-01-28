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

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    enrollment_no = models.CharField(max_length=20, unique=True, null=False, blank=False)
    name = models.CharField(_("Full Name"), max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=11, choices=GENDER)

    college = models.CharField(max_length=10,choices=COLLEGE,default='USICT')
    institute_code = models.IntegerField(default=0)
    program_code = models.IntegerField(default=0)
    course = models.CharField(max_length = 20, choices=COURSE, blank=True, null=True)
    dob = models.DateField(_("Date of birth"), blank=True, null=True)
    admission_year = models.IntegerField(_('Year of Admission'), choices=YEAR_CHOICES, blank=True, null=True)
    fathers_name = models.CharField(max_length=50, null=True, blank=True)
    mothers_name = models.CharField(max_length=50, null=True, blank=True)

    region = models.CharField(max_length=20, choices=REGION, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, blank=True, null=True)
    tweth_marks = models.IntegerField(_("12th marks"), blank=True, null=True)
    mobile = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(9999999999)])



    def __str__(self):
        return self.user.email

class ExtraInfo(models.Model):

    EDUCATION = (
        ('UP TO 5TH', 'UP TO 5TH'),
        ('UP TO 8TH', 'UP TO 8TH'),
        ('UP TO 10TH', 'UP TO 10TH'),
        ('UP TO 12TH', 'UP TO 12TH'),
        ('UP TO UG', 'UP TO UG'),
        ('UP TO PG', 'UP TO PG'),
        ('ANY OTHER', 'ANY OTHER'),
    )

    FAMILY_INCOME = (
        ('< 50,000', '< 50,000'),
        ('50,000 - 1,00,000', '50,000 - 1,00,000'),
        ('1,00,000 - 2,50,000', '1,00,000 - 2,50,000'),
        ('2,50,000 - 4,00,000', '2,50,000 - 4,00,000'),
        ('4,00,000 - 6,00,000', '4,00,000 - 6,00,000'),
        ('6,00,000 - 10,00,000', '6,00,000 - 10,00,000'),
        ('10,00,000 >', '10,00,000 >'),
    )

    SCHOOL_ATTENDED_12TH = (
        ('GOVT', 'GOVT'),
        ('GOVT AIDED', 'GOVT AIDED'),
        ('SELF FINANCING/ UNAIDED', 'SELF FINANCING/ UNAIDED'),
    )

    BOARD = (
        ('CBSE', 'CBSE'),
        ('State Board', 'State Board'),
        ('NIOS', 'NIOS'),
        ('Madarsa', 'Madarsa'),
        ('Other', 'Other'),
    )

    FATHERS_EMPLOYMENT = (
        ('GOVT Service, PSU', 'GOVT Service, PSU'),
        ('Private service', 'Private service'),
        ('Self employed', 'Self employed'),
        ('Professional', 'Professional'),
        ('Casual Labour', 'Casual Labour'),
        ('Farming, Agri-Labour', 'Farming, Agri-Labour'),
        ('Unemployed', 'Unemployed'),
        ('Other', 'Other'),
    )

    MOTHERS_EMPLOYMENT = (
        ('GOVT Service, PSU', 'GOVT Service, PSU'),
        ('Private service', 'Private service'),
        ('Self employed', 'Self employed'),
        ('Professional', 'Professional'),
        ('Casual Labour', 'Casual Labour'),
        ('Farming, Agri-Labour', 'Farming, Agri-Labour'),
        ('House wife', 'House wife'),
        ('Other', 'Other'),
    )

    RELIGION = (
        ('Hindu', 'Hindu'),
        ('Muslim', 'Muslim'),
        ('Sikh', 'Sikh'),
        ('Christain', 'Christain'),
        ('Jain', 'Jain'),
        ('Buddhist', 'Buddhist'),
        ('Parshi', 'Parshi'),
        ('Any other', 'Any other'),
    )

    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=1024, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    fathers_education = models.CharField(max_length=20, choices=EDUCATION, blank=True, null=True)
    mothers_education = models.CharField(max_length=20, choices=EDUCATION, blank=True, null=True)
    family_income = models.CharField(max_length=20, choices=FAMILY_INCOME, blank=True, null=True)
    school_attended_12th = models.CharField(max_length=20, choices=SCHOOL_ATTENDED_12TH, blank=True, null=True)
    board = models.CharField(max_length=20, choices=BOARD, blank=True, null=True)
    aadhar_number = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(9999999999999999)])
    religion = models.CharField(max_length=20, choices=RELIGION, blank=True, null=True)
    fathers_employment = models.CharField(max_length=20, choices=FATHERS_EMPLOYMENT, blank=True, null=True)
    mothers_employment = models.CharField(max_length=20, choices=MOTHERS_EMPLOYMENT, blank=True, null=True)


    def __str__(self):
        return self.student





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
