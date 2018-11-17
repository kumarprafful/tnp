from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .models import StudentProfile, FacultyProfile
from .forms import UserForm, FacultyUserForm, FacultyProfileForm

# Create your views here.
def index(request):
    return render(request, 'account/index.html')

def student_register(request):
    registered = False
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('student:dashboard'))
    elif request.method == 'POST':
        user_form = UserForm(data=request.POST)
       # student_profile_form = StudentProfileForm(data=request.POST)
        if user_form.is_valid(): #and student_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            #student_profile = student_profile_form.save(commit=False)
            #student_profile.user = user
            #student_profile.enrollment_no = user.enrollment_no
            #student_profile.save()
            registered = True
            return HttpResponseRedirect(reverse('account:student_login'))
    else:
        user_form = UserForm()
        #student_profile_form = StudentProfileForm()
    return render(request, 'registration/student_register.html', {'registered': registered, 'user_form': user_form }) #, 'student_profile_form': student_profile_form})

def faculty_register(request):
    registered = False
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    elif request.method == 'POST':
        faculty_user_form = FacultyUserForm(data=request.POST)
        faculty_profile_form = FacultyProfileForm(data=request.POST)
        if faculty_user_form.is_valid() and faculty_profile_form.is_valid():
            faculty = faculty_user_form.save(commit=False)
            faculty.set_password(faculty.password)
            faculty.enrollment_no = faculty.fill_enr_no()
            faculty.is_faculty = True
            faculty.save()

            faculty_profile = faculty_profile_form.save(commit=False)
            faculty_profile.user = faculty
            faculty_profile.save()
            registered = True
            return HttpResponseRedirect(reverse('account:faculty_login'))
    else:
        faculty_user_form = FacultyUserForm()
        faculty_profile_form = FacultyProfileForm()
    return render(request, 'registration/faculty_register.html', {'registered': registered, 'faculty_user_form':faculty_user_form, 'faculty_profile_form': faculty_profile_form})

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_faculty is False:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('student:dashboard'))
                else:
                    return HttpResponseRedirect(reverse('account:student_login'))
            else:
                # write a message for violation
                return HttpResponseRedirect(reverse('account:student_login'))
        else:
            return HttpResponseRedirect(reverse('account:student_login'))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('student:dashboard'))
        else:
            return render(request, 'registration/student_login.html', {})

def faculty_login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_faculty:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('faculty:dashboard'))
                else:
                    return HttpResponseRedirect(reverse('account:faculty_login'))
            else:
                # write a message for user voilation and instead o redirecting to home page we can do something else
                return HttpResponseRedirect(reverse('account:faculty_login'))
        else:
            messages.error(request, "Your email and password didn't match. Please try again.")
            return HttpResponseRedirect(reverse('account:faculty_login'))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('faculty:dashboard'))
        else:
            return render(request, 'registration/faculty_login.html', {})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))
