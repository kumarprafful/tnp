# Generated by Django 2.1.2 on 2019-03-30 20:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190331_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='admission_year',
            field=models.IntegerField(blank=True, choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], null=True, verbose_name='Year of Admission'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='course',
            field=models.CharField(blank=True, choices=[('BtechCSE', 'B.TECH - CSE'), ('BtechIT', 'B.TECH - IT'), ('BtechECE', 'B.TECH - ECE'), ('MtechCSE', 'M.TECH - CSE'), ('MtechIT', 'M.TECH - IT'), ('MtechECE', 'M.TECH - ECE'), ('MCA', 'MCA')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='passing_year',
            field=models.IntegerField(blank=True, choices=[(2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], null=True, verbose_name='Year of Passing Out'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='primary_mobile',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Mobile Number'),
        ),
    ]
