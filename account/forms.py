from django import forms
from .models import User, FacultyProfile
from student.models import StudentProfile


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['enrollment_no', 'email', 'password', 'confirm_password']

class StudentProfileForm(forms.ModelForm):
    # dob = forms.DateField(required = False, widget = DateInput())
    class Meta:
        model = StudentProfile
        fields = ['name', 'course', 'admission_year', 'passing_year', 'primary_mobile']

class FacultyUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'password']

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = FacultyProfile
        fields = []
