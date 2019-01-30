# Generated by Django 2.1.2 on 2019-01-02 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190102_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem1', models.IntegerField(blank=True, null=True)),
                ('sem2', models.IntegerField(blank=True, null=True)),
                ('sem3', models.IntegerField(blank=True, null=True)),
                ('sem4', models.IntegerField(blank=True, null=True)),
                ('sem5', models.IntegerField(blank=True, null=True)),
                ('sem6', models.IntegerField(blank=True, null=True)),
                ('sem7', models.IntegerField(blank=True, null=True)),
                ('sem8', models.IntegerField(blank=True, null=True)),
                ('cgpa', models.IntegerField(blank=True, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.StudentProfile')),
            ],
        ),
    ]