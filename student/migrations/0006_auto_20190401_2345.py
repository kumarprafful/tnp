# Generated by Django 2.1.2 on 2019-04-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20190331_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeeducation',
            name='course',
            field=models.CharField(choices=[('Graduation', 'Graduation'), ('Post-Graduation', 'Post-Graduation'), ('PhD', 'PhD'), ('Diploma', 'Diploma')], max_length=50),
        ),
        migrations.AlterField(
            model_name='schooleducation',
            name='qualification',
            field=models.CharField(blank=True, choices=[('X (Secondary)', 'X (Secondary)'), ('XII (Senior Secondary)', 'XII (Senior Secondary)')], max_length=20, null=True),
        ),
    ]