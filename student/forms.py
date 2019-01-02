from django import forms
from student.models import StudentProfile

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentProfileForm(forms.ModelForm):

    dob = forms.DateField(required = False, widget = DateInput())

    class Meta:
        model = StudentProfile
        fields = ['name', 'college', 'course', 'dob', 'admission_year', 'fathers_name', 'region', 'category', 'mobile']
