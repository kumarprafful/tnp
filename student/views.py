from django.shortcuts import render, get_object_or_404
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
    # StudentProfileForm,
    StudentProfileDashForm,
    MarkSheetForm,
    ExtraInfoForm,
    WorkExperienceForm,
    WorkExperienceEditForm,
    SchoolEducationForm,
    CollegeEducationForm,
    )

# Create your views here.
@login_required(login_url=reverse_lazy('account:student_login'))
def dashboard(request):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    else:
        Student = StudentProfile.objects.get(user=request.user)
        school_education = SchoolEducation.objects.filter(student=Student)
        current_college_education = CollegeEducation.objects.get(student=Student, from_profile=True)
        college_education = CollegeEducation.objects.filter(student=Student, from_profile=False)
        internship = WorkExperience.objects.filter(student=Student, category="Internship")
        project = WorkExperience.objects.filter(student=Student, category="Project")
        training = WorkExperience.objects.filter(student=Student, category="Training")
        achievement = WorkExperience.objects.filter(student=Student, category="Achievement")
        other = WorkExperience.objects.filter(student=Student, category="Other")

        marksheet = MarkSheet.objects.get(student=Student)

        return render(request, template_name='student/student_dashboard.html', context = {
                            'student' : Student,
                            'school_education': school_education,
                            'current_college_education': current_college_education,
                            'college_education': college_education,
                            'internship': internship,
                            'project': project,
                            'training': training,
                            'achievement': achievement,
                            'other': other,
                            'marksheet': marksheet,
                            })

# @login_required(login_url=reverse_lazy('account:student_login'))
# def edit_profile(request):
# 	if request.user.is_faculty:
# 		return HttpResponseRedirect(reverse('faculty:dashboard'))
# 	else:
# 		Student = StudentProfile.objects.get(enrollment_no = request.user.enrollment_no)
#
# 		if request.method == 'POST':
# 			student_profile_form = StudentProfileForm(data=request.POST, instance = Student)
# 			if student_profile_form.is_valid():
# 				student_profile_form.save()
# 				return HttpResponseRedirect(reverse('student:dashboard'))
#
# 		else:
# 			student_profile_form = StudentProfileForm(instance=Student)
# 		return render(request, template_name='student/edit_profile.html', context = {'student_profile_form': student_profile_form})
#
#
# def createMarkSheetView(request):
#     if request.user.is_faculty:
#         return HttpResponseRedirect(reverse('faculty:dashboard'))
#     else:
#         marksheet_added = False
#         student = StudentProfile.objects.get(enrollment_no = request.user.enrollment_no)
#         marks = MarkSheet.objects.get(student=student)
#         if request.method == 'POST':
#             marksheet_form = MarkSheetForm(data=request.POST, instance=marks)
#             if marksheet_form.is_valid():
#                 marksheet =  marksheet_form.save(commit=False)
#                 marksheet.student = student
#                 marksheet.save()
#                 marksheet_added = True
#                 return HttpResponseRedirect(reverse('student:dashboard'))
#         else:
#             marksheet_form = MarkSheetForm(instance=marks)
#         return render(request, 'student/add_marksheet.html', {'marksheet_form': marksheet_form, 'marksheet_added': marksheet_added})
#
#
# def createExtraInfoView(request):
#     if request.user.is_faculty:
#         return HttpResponseRedirect(reverse('faculty:dashboard'))
#     else:
#         extra_info_added = False
#         student = StudentProfile.objects.get(enrollment_no = request.user.enrollment_no)
#         info = ExtraInfo.objects.get(student=student)
#         if request.method == 'POST':
#             extra_info_form = ExtraInfoForm(data=request.POST, instance=info)
#             if extra_info_form.is_valid():
#                 extra_info =  extra_info_form.save(commit=False)
#                 extra_info.student = student
#                 extra_info.save()
#                 extra_info_added = True
#                 return HttpResponseRedirect(reverse('student:dashboard'))
#         else:
#             extra_info_form = ExtraInfoForm(instance=info)
#         return render(request, 'student/add_extra_info.html', {'extra_info_form': extra_info_form, 'extra_info_added': extra_info_added})
#
#
# def WorkExperienceView(request):
#     if request.user.is_faculty:
#         return HttpResponseRedirect(reverse('faculty:dashboard'))
#
#     else:
#         student = StudentProfile.objects.get(enrollment_no = request.user.enrollment_no)
#         if request.method == 'POST':
#             work_experience_form = WorkExperienceForm(request.POST)
#             if work_experience_form.is_valid():
#                 work_experience = work_experience_form.save(commit=False)
#                 work_experience.student = student
#                 work_experience.save()
#
#                 return HttpResponseRedirect(reverse('student:work_experience'))
#
#         work_experience_all = WorkExperience.objects.filter(student = student)
#         work_experience_form = WorkExperienceForm()
#         context = {
#             'work_experience_all' : work_experience_all,
#             'work_experience_form' : work_experience_form,
#         }
#
#         return render(request, 'student/work_experience.html', context)
#
# def deleteWorkExperienceView(request, pk):
#     instance = WorkExperience.objects.get(pk=pk)
#     instance.delete()
#     return HttpResponse('deletion successful')

def schoolEducation(request,pk):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    else:
        student = StudentProfile.objects.get(enrollment_no=request.user.enrollment_no)
        school_edu = SchoolEducation.objects.get(student=student ,pk=pk)
        if request.method == 'POST':
            school_education = SchoolEducationForm(data=request.POST, instance=school_edu)
            if school_education.is_valid():
                edu = school_education.save(commit=False)
                edu.student = student
                edu.save()
                return HttpResponse('Form Submitted')
            else:
                return HttpResponse('INVALID FORM')
        else:
            school_education = SchoolEducationForm(instance=school_edu)
        return HttpResponse(school_education.as_p())

# def collegeEducation(request):
#     if request.user.is_faculty:
#         return HttpResponseRedirect(reverse('faculty:dashboard'))
#     else:
#         student = StudentProfile.objects.get(enrollment_no=request.user.enrollment_no)
#         if request.method == 'POST':
#             college_education = CollegeEducationForm(data=request.POST)
#             if college_education.is_valid():
#                 edu = college_education.save(commit=False)
#                 edu.student = student
#                 edu.save()
#                 return HttpResponse('Form Submitted')
#             else:
#                 return HttpResponse('INVALID FORM')
#         else:
#             college_education = CollegeEducationForm()
#             return HttpResponse(college_education.as_p())
#

def studentProfileDashView(request):
    student = StudentProfile.objects.get(enrollment_no=request.user.enrollment_no)
    if request.method == 'POST':
        studentProfile = StudentProfileDashForm(data=request.POST, instance=student)
        if studentProfile.is_valid():
            studentProfile.save()
            return HttpResponse('Form submitted')
        else:
            return HttpResponse('INVALID FORM')

    else:
        studentProfile = StudentProfileDashForm(instance=student)
        return HttpResponse(studentProfile.as_p())

def workExperienceDashView(request, category=None):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    else:
        student = StudentProfile.objects.get(enrollment_no=request.user.enrollment_no)
        if request.method == 'POST':
            work_exp = WorkExperienceForm(data=request.POST)
            if work_exp.is_valid():
                edu = work_exp.save(commit=False)
                edu.student = student
                edu.save()
                return HttpResponse('Form Submitted')
            # else:
            #     return HttpResponse('INVALID FORM')
        else:
            data = {'category': category}
            work_exp = WorkExperienceForm(initial=data)
    return HttpResponse(work_exp.as_p())

def editWorkExperienceDashView(request, pk):
    student = StudentProfile.objects.get(enrollment_no = request.user.enrollment_no)
    instance = WorkExperience.objects.get(student=student, pk=pk)
    print("THIS")
    if request.method == 'POST':
        work_experience_form = WorkExperienceEditForm(data=request.POST, instance=instance)
        if work_experience_form.is_valid():
            work_experience_form.save()
            return HttpResponse('Form Submitted')
    else:
        work_experience_form = WorkExperienceEditForm(instance=instance)
    return HttpResponse(work_experience_form.as_p())

def workExperienceDelete(request, pk):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    else:
        student = StudentProfile.objects.get(enrollment_no=request.user.enrollment_no)
        work_exp = WorkExperience.objects.get(student=student, pk=pk)
        work_exp.delete()
        return HttpResponse('Deleted')


def collegeEducationDashView(request, course=None):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    else:
        student = StudentProfile.objects.get(enrollment_no=request.user.enrollment_no)
        if request.method == 'POST':
            college_edu = CollegeEducationForm(data=request.POST)
            if college_edu.is_valid():
                edu = college_edu.save(commit=False)
                edu.student = student
                edu.save()
                return HttpResponse('Form Submitted')
            else:
                return HttpResponse('INVALID FORM')
        else:
            data = {'course': course}
            college_edu = CollegeEducationForm(initial=data)
        return HttpResponse(college_edu.as_p())

def collegeEducationEdit(request, pk):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    else:
        student = StudentProfile.objects.get(enrollment_no=request.user.enrollment_no)
        college_education = CollegeEducation.objects.get(student=student, pk=pk)
        if request.method == 'POST':
            college_edu = CollegeEducationForm(data=request.POST, instance=college_education)
            if college_edu.is_valid():
                edu = college_edu.save(commit=False)
                edu.save()
                return HttpResponse('Form Submitted')
            else:
                return HttpResponse('INVALID FORM')
        else:
            college_edu = CollegeEducationForm(instance=college_education)
        return HttpResponse(college_edu.as_p())

def collegeEducationDelete(request, pk):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    else:
        student = StudentProfile.objects.get(enrollment_no=request.user.enrollment_no)
        college_education = CollegeEducation.objects.get(student=student, pk=pk)
        college_education.delete()
        return HttpResponse('Deleted')

def marksheetEdit(request, pk):
    if request.user.is_faculty:
        return HttpResponseRedirect(reverse('faculty:dashboard'))
    else:
        student = StudentProfile.objects.get(enrollment_no=request.user.enrollment_no)
        marksheet = MarkSheet.objects.get(student=student, pk=pk)
        if request.method == 'POST':
            marksheet_form = MarkSheetForm(data=request.POST, instance=marksheet)
            if marksheet_form.is_valid():
                edu = marksheet_form.save(commit=False)
                edu.save()
                return HttpResponse('Form Submitted')
            else:
                return HttpResponse('INVALID FORM')
        else:
            marksheet_form = MarkSheetForm(instance=marksheet)
            return HttpResponse(marksheet_form.as_p())
