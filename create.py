from account.models import User
from student.models import StudentProfile
from faker import Faker
import random, string
import datetime

fake = Faker()

x = ''.join(random.choices(string.digits, k=10))

courses = ['B.TECH - CSE', 'B.TECH - IT', 'B.TECH - ECE', 'M.TECH - CSE', 'M.TECH - IT', 'M.TECH - ECE', 'MCA']
region = ['Delhi', 'Outside Delhi']
category = ['Unreserved', 'OBC', 'SC', 'ST', 'Other']


COLLEGE = ('USICT')

COURSE = (
        'BtechCSE',
        'BtechIT',
        'BtechECE',
        'MtechCSE',
        'MtechIT',
        'MtechECE',
        'MCA',
    )

YEAR_CHOICES = []
for r in range(2015, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append(r)

REGION = (
        'DEL',
        'ODEL',
    )

CATEGORY = (
        'UR',
        'OBC',
        'SC',
        'ST',
        'OTH',
    )


def choose(para):
    return random.choices(para)[0]


for i in range(100):
    u = User.objects.create(id=i+400, enrollment_no=x+str(i), email=fake.free_email())
    StudentProfile.objects.create(
                                user=u,
                                enrollment_no=u.enrollment_no,
                                name=fake.name(),
                                course=choose(COURSE),
                                dob=fake.date_between(start_date="-20y", end_date="-18y"),
                                admission_year=choose(YEAR_CHOICES),
                                fathers_name=fake.name(),
                                region=choose(REGION),
                                category=choose(CATEGORY),
                                mobile=989898989
                                )
