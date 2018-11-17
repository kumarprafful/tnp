from django import forms
from .models import User, StudentProfile, FacultyProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['enrollment_no', 'email', 'password']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['college', 'course', 'dob', 'admission_year', 'fathers_name', 'region', 'category', 'mobile']


class FacultyUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'password']

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = FacultyProfile
        fields = []
