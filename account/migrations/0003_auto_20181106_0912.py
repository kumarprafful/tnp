# Generated by Django 2.1.2 on 2018-11-06 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_is_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_faculty',
            field=models.BooleanField(default=False, help_text="Designates whether the account is of student's or faculty"),
        ),
    ]
