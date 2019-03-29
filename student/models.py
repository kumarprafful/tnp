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

    ADMISSION_YEAR_CHOICES = []
    for r in range((datetime.now().year-4), (datetime.now().year+1)):
        ADMISSION_YEAR_CHOICES.append((r,r))

    PASSING_YEAR_CHOICES = []
    for r in range((datetime.now().year), (datetime.now().year+5)):
        PASSING_YEAR_CHOICES.append((r,r))

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
    name = models.CharField(_("Full Name"), max_length=100)
    gender = models.CharField(max_length=11, choices=GENDER)
    dob = models.DateField(_("Date of birth"), blank=True, null=True)
    college = models.CharField(max_length=10,choices=COLLEGE,default='USICT')
    #institute_code = models.IntegerField(default=0)
    #program_code = models.IntegerField(default=0)
    course = models.CharField(max_length = 20, choices=COURSE)
    admission_year = models.IntegerField(_('Year of Admission'), blank=True, null=True, choices=ADMISSION_YEAR_CHOICES)
    passing_year = models.IntegerField(_('Year of Passing Out'), blank=True, null=True, choices=PASSING_YEAR_CHOICES)
    fathers_name = models.CharField(max_length=100)
    region = models.CharField(max_length=20, choices=REGION)
    category = models.CharField(max_length=20, choices=CATEGORY)
    primary_mobile = models.PositiveIntegerField(_("Mobile Number"), blank=True, null=True, validators=[MaxValueValidator(9999999999)])
    secondary_mobile = models.PositiveIntegerField(_("Alternative Mobile Number"), blank=True, null=True, validators=[MaxValueValidator(9999999999)])
    address = models.TextField(max_length=200, blank=True, null=True)

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
        return self.student.enrollment_no

class MarkSheet(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    semester_1 = models.DecimalField(max_digits=5, decimal_places=3, validators=[MaxValueValidator(10.000),MinValueValidator(0.000)],blank=True, null=True)
    semester_2 = models.DecimalField(max_digits=5, decimal_places=3, validators=[MaxValueValidator(10.000),MinValueValidator(0.000)],blank=True, null=True)
    semester_3 = models.DecimalField(max_digits=5, decimal_places=3, validators=[MaxValueValidator(10.000),MinValueValidator(0.000)],blank=True, null=True)
    semester_4 = models.DecimalField(max_digits=5, decimal_places=3, validators=[MaxValueValidator(10.000),MinValueValidator(0.000)],blank=True, null=True)
    semester_5 = models.DecimalField(max_digits=5, decimal_places=3, validators=[MaxValueValidator(10.000),MinValueValidator(0.000)],blank=True, null=True)
    semester_6 = models.DecimalField(max_digits=5, decimal_places=3, validators=[MaxValueValidator(10.000),MinValueValidator(0.000)],blank=True, null=True)
    semester_7 = models.DecimalField(max_digits=5, decimal_places=3, validators=[MaxValueValidator(10.000),MinValueValidator(0.000)],blank=True, null=True)
    semester_8 = models.DecimalField(max_digits=5, decimal_places=3, validators=[MaxValueValidator(10.000),MinValueValidator(0.000)],blank=True, null=True)
    cgpa = models.DecimalField(max_digits=5, decimal_places=3, validators=[MaxValueValidator(10.000),MinValueValidator(0.000)],blank=True, null=True)

    credits_skipped = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    backlogs = models.IntegerField(verbose_name = "Number of Backlogs", validators=[MinValueValidator(0)], blank=True, null=True)

    def __str__(self):
        return self.student.enrollment_no
        #return "%s "%s" % (self.student.enrollment_no, self.student.name)

class WorkExperience(models.Model):

    CATEGORY_CHOICE =(
        ('Internship', 'Internship'),
        ('Project', 'Project'),
        ('Training', 'Training'),
        ('Achievement', 'Achievement'),
        ('Other', 'Other'),
    )

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    category = models.CharField(choices = CATEGORY_CHOICE, max_length = 15, null=True)
    title = models.CharField(max_length = 50, null=True)
    start_date = models.DateField(_("Starting Date"), null=True)
    end_date = models.DateField(_("Ending Date"), blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(max_length = 200, null=True)

    def __str__(self):
        return self.student.enrollment_no

class SchoolEducation(models.Model):

    QUALIFICATON_CHOICE = (
        ('HighSchool', 'High School'),
        ('SeniorSecondary', 'Senior Secondary'),
    )

    YEAR_CHOICES = []
    for r in range((datetime.now().year-15), (datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    qualificaion = models.CharField(choices=QUALIFICATON_CHOICE, max_length=20, null=True)
    year = models.IntegerField(choices=YEAR_CHOICES, null=True, blank=True)
    board = models.CharField(max_length=50, null=True, blank=True)
    school = models.CharField(max_length=100, null=True, blank=True)
    marks = models.CharField(_("Percentage/CGPA"), max_length=5, null=True, blank=True)

    def __str__(self):
        return self.student.enrollment_no

class CollegeEducation(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, null=True, blank=True)
    branch = models.CharField(max_length=50, null=True, blank=True)
    college = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(_("Starting Date"), null=True)
    end_date = models.DateField(_("Ending Date"), blank=True, null=True)
    marks = models.DecimalField(_("Aggregate Marks/CGPA"), max_digits=5, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return self.student.enrollment_no
