from account.models import User, StudentProfile
from faker import Faker
import random, string

fake = Faker()

x = ''.join(random.choices(string.digits, k=10))

courses = ['B.TECH - CSE', 'B.TECH - IT', 'B.TECH - ECE', 'M.TECH - CSE', 'M.TECH - IT', 'M.TECH - ECE', 'MCA']
region = ['Delhi', 'Outside Delhi']
category = ['Unreserved', 'OBC', 'SC', 'ST', 'Other']

def choose(para):
    return random.choices(para)[0]


for i in range(50):
    u = User.objects.create(id=i+400, enrollment_no=x+str(i), email=fake.free_email())
    StudentProfile.objects.create(
                                user=u,
                                enrollment_no=u.enrollment_no,
                                name=fake.name(),
                                course=choose(courses),
                                dob=fake.date_between(start_date="-20y", end_date="-18y"),
                                admission_year=fake.date_between(start_date="-10y", end_date="today"),
                                fathers_name=fake.name(),
                                region=choose(region),
                                category=choose(category),
                                mobile=989898989
                                )
