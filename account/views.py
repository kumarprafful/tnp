from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError
from student.models import (
    StudentProfile,
    MarkSheet,
    ExtraInfo,
    WorkExperience,
    SchoolEducation,
    CollegeEducation,
    )
from account.models import FacultyProfile
from account.forms import UserForm, FacultyUserForm, FacultyProfileForm, StudentProfileForm

from .tokens import account_activation_token
from .models import User

# Create your views here.
def index(request):
    return render(request, 'account/index.html')

def student_register(request):
    registered = False
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('student:dashboard'))
    elif request.method == 'POST':
        user_form = UserForm(data=request.POST)
        student_profile_form = StudentProfileForm(data=request.POST)
        if user_form.is_valid() and student_profile_form.is_valid():

            if user_form.cleaned_data['password'] != user_form.cleaned_data['confirm_password']:
                messages.error(request, 'Password and confirm password does not match.')
                return HttpResponseRedirect(reverse('account:student_register'))

            else:
                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.is_active = False
                user.save()

                # user.save(commit=False)
                student_profile = student_profile_form.save(commit=False)
                # student_profile = StudentProfile.objects.create(user = user)
                student_profile.user = user
                student_profile.enrollment_no = user.enrollment_no
                student_profile.save()
                MarkSheet.objects.create(student=student_profile)
                ExtraInfo.objects.create(student=student_profile)
                WorkExperience.objects.create(student=student_profile)
                SchoolEducation.objects.create(student=student_profile,qualification="X (Secondary)")
                SchoolEducation.objects.create(student=student_profile,qualification="XII (Senior Secondary)")
                CollegeEducation.objects.create(
                                    student=student_profile,
                                    from_profile=True,
                                    course=student_profile.course,
                                    start_date=student_profile.admission_year,
                                    end_date=student_profile.passing_year,
                                    college=student_profile.college
                                    )


                registered = True
                print(user)
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('registration/email_activate.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token':account_activation_token.make_token(user),
                })
                to_email = user.email
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                email.send()

                return render(request, 'registration/email_activate_done.html')
    else:
        user_form = UserForm()
        student_profile_form = StudentProfileForm()
    return render(request, 'registration/student_register.html', {'registered': registered, 'user_form': user_form, 'student_profile_form': student_profile_form})

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
                    messages.error(request, 'Account not active. Please check email inbox for activation link or contact TNP cell.')
                    return HttpResponseRedirect(reverse('account:student_login'))
            else:
                # write a message for violation
                messages.error(request, 'Invalid credentials. Try again.')
                return HttpResponseRedirect(reverse('account:student_login'))
        else:
            messages.error(request, 'Invalid credentials. Try again.')
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
                    messages.error(request, 'Account not active. Kindly contact TNP cell')
                    return HttpResponseRedirect(reverse('account:faculty_login'))
            else:
                messages.error(request, "Your email and password didn't match. Please try again.")
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
    return HttpResponseRedirect(reverse('account:student_login'))


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        user_profile = UserProfile.objects.get(user=user)
    except:
        user_profile=None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account activation successful. Please login to continue')
        return HttpResponseRedirect(reverse('student:dashboard'))
    else:
        return HttpResponse('Activation link is invalid!')
