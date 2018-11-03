from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import StudentProfile, FacultyProfile
from .forms import UserForm, StudentProfileForm

# Create your views here.
def index(request):
    return render(request, 'account/index.html')

def student_register(request):
    registered = False
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    elif request.method == 'POST':
        user_form = UserForm(data=request.POST)
        student_profile_form = StudentProfileForm(data=request.POST)
        if user_form.is_valid() and student_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            student_profile = student_profile_form.save(commit=False)
            student_profile.user = user
            student_profile.save()
            registered = True
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Invalid form data. Kindly fill the form with correct credentials')
            return HttpResponseRedirect(reverse('student_register'))
    else:
        user_form = UserForm()
        student_profile_form = StudentProfileForm()
    return render(request, 'registration/student_register.html', {'registered': registered, 'user_form': user_form, 'student_profile_form': student_profile_form})

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.warning(request, "Account is inactive")
                return HttpResponseRedirect(reverse('student_login'))
        else:
            messages.error(request, "invalid credentials")
            return HttpResponseRedirect(reverse('student_login'))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'registration/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
