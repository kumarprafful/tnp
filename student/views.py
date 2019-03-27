from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

from student.models import (
    StudentProfile,
    MarkSheet,
    ExtraInfo,
    WorkExperience,
    SchoolEducation,
    CollegeEducation,
    )

from student.forms import(
    StudentProfileForm,
    MarkSheetForm,
    ExtraInfoForm, 
    WorkExperienceForm, 
    SchoolEducationForm, 
    CollegeEducationForm,
    )

# Create your views here.
@login_required(login_url=reverse_lazy('account:student_login'))
def dashboard(request):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    else:
    	Student = StudentProfile.objects.get(enrollment_no = request.user.enrollment_no)

    	return render(request, template_name='student/student_dashboard.html', context = {'Student' : Student})


@login_required(login_url=reverse_lazy('account:student_login'))
def edit_profile(request):
	if request.user.is_faculty:
		return HttpResponseRedirect(reverse('faculty:dashboard'))
	else:
		Student = StudentProfile.objects.get(enrollment_no = request.user.enrollment_no)

		if request.method == 'POST':
			student_profile_form = StudentProfileForm(data=request.POST, instance = Student)
			if student_profile_form.is_valid():
				student_profile_form.save()
				return HttpResponseRedirect(reverse('student:dashboard'))

		else:
			student_profile_form = StudentProfileForm(instance=Student)
		return render(request, template_name='student/edit_profile.html', context = {'student_profile_form': student_profile_form})


def createMarkSheetView(request):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    else:
        marksheet_added = False
        student = StudentProfile.objects.get(enrollment_no = request.user.enrollment_no)
        marks = MarkSheet.objects.get(student=student)
        if request.method == 'POST':
            marksheet_form = MarkSheetForm(data=request.POST, instance=marks)
            if marksheet_form.is_valid():
                marksheet =  marksheet_form.save(commit=False)
                marksheet.student = student
                marksheet.save()
                marksheet_added = True
                return HttpResponseRedirect(reverse('student:dashboard'))
        else:
            marksheet_form = MarkSheetForm(instance=marks)
        return render(request, 'student/add_marksheet.html', {'marksheet_form': marksheet_form, 'marksheet_added': marksheet_added})


def createExtraInfoView(request):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    else:
        extra_info_added = False
        student = StudentProfile.objects.get(enrollment_no = request.user.enrollment_no)
        info = ExtraInfo.objects.get(student=student)
        if request.method == 'POST':
            extra_info_form = ExtraInfoForm(data=request.POST, instance=info)
            if extra_info_form.is_valid():
                extra_info =  extra_info_form.save(commit=False)
                extra_info.student = student
                extra_info.save()
                extra_info_added = True
                return HttpResponseRedirect(reverse('student:dashboard'))
        else:
            extra_info_form = ExtraInfoForm(instance=info)
        return render(request, 'student/add_extra_info.html', {'extra_info_form': extra_info_form, 'extra_info_added': extra_info_added})


def WorkExperienceView(request):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))

    else:
        student = StudentProfile.objects.get(enrollment_no = request.user.enrollment_no)
        if request.method == 'POST':
            work_experience_form = WorkExperienceForm(request.POST)
            if work_experience_form.is_valid():
                print('i was here lllalalal')
                work_experience = work_experience_form.save(commit=False)
                work_experience.student = student
                work_experience.save()

                return HttpResponseRedirect(reverse('student:work_experience'))

        work_experience_all = WorkExperience.objects.filter(student = student)
        work_experience_form = WorkExperienceForm()
        context = {
            'work_experience_all' : work_experience_all,
            'work_experience_form' : work_experience_form,
        }
        
        return render(request, 'student/work_experience.html', context)

def editWorkExperienceView(request, pk):
    print(request)
    student = StudentProfile.objects.get(enrollment_no = request.user.enrollment_no)
    instance = WorkExperience.objects.get(pk=pk)
    if request.method == 'POST':
        print("i Think it nuttts")
        work_experience_form = WorkExperienceForm(data=request.POST, instance=instance)
        if work_experience_form.is_valid():
            print('i was here ollaaa')
            work_experience_form.save()
            return HttpResponse('edit successful')

    else:
        print("i am gonna ")
        student_profile_form = WorkExperienceForm(instance=instance)
        return HttpResponse(student_profile_form.as_p())


def deleteWorkExperienceView(request, pk):
    instance = WorkExperience.objects.get(pk=pk)
    instance.delete()
    return HttpResponse('deletion successful')


def education(request):
    return render(request, 'student/education.html')