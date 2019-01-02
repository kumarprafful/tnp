from django import forms
from .models import User, FacultyProfile


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['enrollment_no', 'email', 'password']

class FacultyUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'password']

class FacultyProfileForm(forms.ModelForm):
    class Meta:
        model = FacultyProfile
        fields = []
