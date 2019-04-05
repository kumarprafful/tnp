# Generated by Django 2.1.2 on 2019-03-01 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20190301_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.StudentProfile')),
            ],
        ),
        migrations.RenameField(
            model_name='marksheet',
            old_name='CGPA',
            new_name='cgpa',
        ),
    ]