# Generated by Django 2.1.2 on 2018-11-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20181115_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='enrollment_no',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='enrollment_no',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
