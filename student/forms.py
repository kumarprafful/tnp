from django import forms
from django.forms.widgets import HiddenInput
from student.models import (
    StudentProfile,
    MarkSheet,
    ExtraInfo,
    WorkExperience,
    SchoolEducation,
    CollegeEducation,
    )
class DateInput(forms.DateInput):
    input_type = 'date'


class StudentProfileDashForm(forms.ModelForm):
    dob = forms.DateField(required = False, widget = DateInput())

    class Meta:
        model = StudentProfile
        exclude = ['user', 'enrollment_no', 'college',]

class StudentProfileForm(forms.ModelForm):

    dob = forms.DateField(required = False, widget = DateInput())

    class Meta:
        model = StudentProfile
        exclude = ['user', 'enrollment_no',]

class MarkSheetForm(forms.ModelForm):

    class Meta:
        model = MarkSheet
        exclude = ['student',]

class ExtraInfoForm(forms.ModelForm):
    class Meta:
        model = ExtraInfo
        exclude = ['student',]

class WorkExperienceForm(forms.ModelForm):

    start_date = forms.DateField(required = False, widget = DateInput())
    end_date = forms.DateField(required = False, widget = DateInput())
    category = forms.CharField(widget=HiddenInput)

    class Meta:
        model = WorkExperience
        exclude = ['student',]


class SchoolEducationForm(forms.ModelForm):
    class Meta:
        model = SchoolEducation
        exclude = ['student',]

class CollegeEducationForm(forms.ModelForm):
    class Meta:
        model = CollegeEducation
        exclude = ['student',]
