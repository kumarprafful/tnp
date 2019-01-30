from django import forms
from student.models import StudentProfile, MarkSheet, ExtraInfo

class DateInput(forms.DateInput):
    input_type = 'date'

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
