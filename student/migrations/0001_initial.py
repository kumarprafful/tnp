# Generated by Django 2.1.2 on 2019-01-30 09:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=1024, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('fathers_education', models.CharField(blank=True, choices=[('UP TO 5TH', 'UP TO 5TH'), ('UP TO 8TH', 'UP TO 8TH'), ('UP TO 10TH', 'UP TO 10TH'), ('UP TO 12TH', 'UP TO 12TH'), ('UP TO UG', 'UP TO UG'), ('UP TO PG', 'UP TO PG'), ('ANY OTHER', 'ANY OTHER')], max_length=20, null=True)),
                ('mothers_education', models.CharField(blank=True, choices=[('UP TO 5TH', 'UP TO 5TH'), ('UP TO 8TH', 'UP TO 8TH'), ('UP TO 10TH', 'UP TO 10TH'), ('UP TO 12TH', 'UP TO 12TH'), ('UP TO UG', 'UP TO UG'), ('UP TO PG', 'UP TO PG'), ('ANY OTHER', 'ANY OTHER')], max_length=20, null=True)),
                ('family_income', models.CharField(blank=True, choices=[('< 50,000', '< 50,000'), ('50,000 - 1,00,000', '50,000 - 1,00,000'), ('1,00,000 - 2,50,000', '1,00,000 - 2,50,000'), ('2,50,000 - 4,00,000', '2,50,000 - 4,00,000'), ('4,00,000 - 6,00,000', '4,00,000 - 6,00,000'), ('6,00,000 - 10,00,000', '6,00,000 - 10,00,000'), ('10,00,000 >', '10,00,000 >')], max_length=20, null=True)),
                ('school_attended_12th', models.CharField(blank=True, choices=[('GOVT', 'GOVT'), ('GOVT AIDED', 'GOVT AIDED'), ('SELF FINANCING/ UNAIDED', 'SELF FINANCING/ UNAIDED')], max_length=20, null=True)),
                ('board', models.CharField(blank=True, choices=[('CBSE', 'CBSE'), ('State Board', 'State Board'), ('NIOS', 'NIOS'), ('Madarsa', 'Madarsa'), ('Other', 'Other')], max_length=20, null=True)),
                ('aadhar_number', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999999999)])),
                ('religion', models.CharField(blank=True, choices=[('Hindu', 'Hindu'), ('Muslim', 'Muslim'), ('Sikh', 'Sikh'), ('Christain', 'Christain'), ('Jain', 'Jain'), ('Buddhist', 'Buddhist'), ('Parshi', 'Parshi'), ('Any other', 'Any other')], max_length=20, null=True)),
                ('fathers_employment', models.CharField(blank=True, choices=[('GOVT Service, PSU', 'GOVT Service, PSU'), ('Private service', 'Private service'), ('Self employed', 'Self employed'), ('Professional', 'Professional'), ('Casual Labour', 'Casual Labour'), ('Farming, Agri-Labour', 'Farming, Agri-Labour'), ('Unemployed', 'Unemployed'), ('Other', 'Other')], max_length=20, null=True)),
                ('mothers_employment', models.CharField(blank=True, choices=[('GOVT Service, PSU', 'GOVT Service, PSU'), ('Private service', 'Private service'), ('Self employed', 'Self employed'), ('Professional', 'Professional'), ('Casual Labour', 'Casual Labour'), ('Farming, Agri-Labour', 'Farming, Agri-Labour'), ('House wife', 'House wife'), ('Other', 'Other')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MarkSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_1', models.IntegerField(blank=True, null=True)),
                ('semester_2', models.IntegerField(blank=True, null=True)),
                ('semester_3', models.IntegerField(blank=True, null=True)),
                ('semester_4', models.IntegerField(blank=True, null=True)),
                ('semester_5', models.IntegerField(blank=True, null=True)),
                ('semester_6', models.IntegerField(blank=True, null=True)),
                ('semester_7', models.IntegerField(blank=True, null=True)),
                ('semester_8', models.IntegerField(blank=True, null=True)),
                ('CGPA', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_no', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], max_length=11)),
                ('college', models.CharField(choices=[('USICT', 'U.S.I.C.T.')], default='USICT', max_length=10)),
                ('institute_code', models.IntegerField(default=0)),
                ('program_code', models.IntegerField(default=0)),
                ('course', models.CharField(choices=[('BtechCSE', 'B.TECH - CSE'), ('BtechIT', 'B.TECH - IT'), ('BtechECE', 'B.TECH - ECE'), ('MtechCSE', 'M.TECH - CSE'), ('MtechIT', 'M.TECH - IT'), ('MtechECE', 'M.TECH - ECE'), ('MCA', 'MCA')], max_length=20)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('admission_year', models.CharField(blank=True, choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], max_length=10, null=True, verbose_name='Year of Admission')),
                ('fathers_name', models.CharField(max_length=50)),
                ('mothers_name', models.CharField(max_length=50)),
                ('region', models.CharField(choices=[('DEL', 'Delhi'), ('ODEL', 'Outside Delhi')], max_length=20)),
                ('category', models.CharField(choices=[('UR', 'Unreserved'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('OTH', 'Other')], max_length=20)),
                ('tweth_marks', models.IntegerField(blank=True, null=True, verbose_name='12th marks')),
                ('mobile', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student Profile',
            },
        ),
        migrations.AddField(
            model_name='marksheet',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.StudentProfile'),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.StudentProfile'),
        ),
    ]
