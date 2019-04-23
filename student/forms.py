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
    date_of_birth = forms.DateField(required = True, widget = DateInput())

    class Meta:
        model = StudentProfile
        exclude = ['user', 'enrollment_no', 'college', 'course', 'admission_year','passing_year', 'name']
        widgets = {
            'fathers_name': forms.TextInput(attrs={'required': 'true', 'placeholder': 'Father\'s name'}),
            'primary_mobile': forms.TextInput(attrs={'required': 'true', 'placeholder': 'Mobile number'}),
            'secondary_mobile': forms.TextInput(attrs={'placeholder': 'Alternate mobile number'}),
            'address': forms.Textarea(attrs={'required': 'true', 'placeholder': 'Address'}),

        }

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
        widgets = {
            'title': forms.TextInput(attrs={'required': 'true', 'placeholder': 'Title or company name'}),
            # 'url': forms.TextInp       ut(attrs={'required': 'true', 'placeholder': 'School name'}),
            # '': forms.TextInput(attrs={'placeholder': 'Alternate mobile number'}),
            'description': forms.Textarea(attrs={'required': 'true', 'placeholder': 'Describe your experience'}),
        }


class WorkExperienceEditForm(forms.ModelForm):
    start_date = forms.DateField(required = False, widget = DateInput())
    end_date = forms.DateField(required = False, widget = DateInput())

    class Meta:
        model = WorkExperience
        exclude = ['student', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'required': 'true', 'placeholder': 'Title or company name'}),
            # 'url': forms.TextInp       ut(attrs={'required': 'true', 'placeholder': 'School name'}),
            # '': forms.TextInput(attrs={'placeholder': 'Alternate mobile number'}),
            'description': forms.Textarea(attrs={'required': 'true', 'placeholder': 'Describe your experience'}),

        }


class SchoolEducationForm(forms.ModelForm):
    class Meta:
        model = SchoolEducation
        exclude = ['student', 'qualification']
        widgets = {
            'board': forms.TextInput(attrs={'required': 'true', 'placeholder': 'School board'}),
            'school': forms.TextInput(attrs={'required': 'true', 'placeholder': 'School name'}),
            # '': forms.TextInput(attrs={'placeholder': 'Alternate mobile number'}),
            'marks': forms.TextInput(attrs={'required': 'true', 'placeholder': 'Percentage or CGPA'}),

        }

class CollegeEducationForm(forms.ModelForm):
    course = forms.CharField(widget=HiddenInput)

    class Meta:
        model = CollegeEducation
        exclude = ['student', 'from_profile']
        widgets = {
            'branch': forms.TextInput(attrs={'required': 'true', 'placeholder': 'Course name'}),
            'college': forms.TextInput(attrs={'required': 'true', 'placeholder': 'College name'}),
            # '': forms.TextInput(attrs={'placeholder': 'Alternate mobile number'}),
            'marks': forms.NumberInput(attrs={'required': 'true', 'placeholder': 'Percentage or CGPA', 'step': 0.01}),

        }
