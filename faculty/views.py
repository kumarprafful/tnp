from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers
from account.models import User
from student.models import (
    StudentProfile,
    MarkSheet,
    ExtraInfo,
    WorkExperience,
    SchoolEducation,
    CollegeEducation,
    )

# Create your views here.
@login_required(login_url=reverse_lazy('account:faculty_login'))
def dashboard(request):
    if request.user.is_faculty is False:
        return HttpResponseRedirect(reverse('student:dashboard'))
    else:
    	Students = StudentProfile.objects.all()
    	return render(request, template_name='faculty/faculty_dashboard.html', context = {'Students' : Students })

@login_required(login_url=reverse_lazy('account:faculty_login'))
def filter(request):
	if request.user.is_faculty is False:
		return HttpResponseRedirect(reverse('student:dashboard'))
	else:
		selected_courses = json.loads(request.GET.get('selected_courses'))
		selected_years = json.loads(request.GET.get('selected_years'))


		course_filter = []
		if selected_courses:
			for i in selected_courses:
				course_filter += StudentProfile.objects.filter(course = i)
		else:
			course_filter = StudentProfile.objects.all()

		year_filter = []
		for i in course_filter:
			if selected_years:
				for j in selected_years:
					if str(i.passing_year) == j:
						year_filter += StudentProfile.objects.filter(enrollment_no = i.enrollment_no).values()
						break
			else:
				year_filter += StudentProfile.objects.filter(enrollment_no = i.enrollment_no).values()

		for i in year_filter:
			this_user = User.objects.get(id=i['user_id'])
			this_student = StudentProfile.objects.get(id=i['id'])
			email = this_user.email
			i['email'] = email
			i['course'] = this_student.get_course_display()

		data = {
			'filtered_students': year_filter
		}


		return JsonResponse(data, safe=False)

@login_required(login_url=reverse_lazy('account:faculty_login'))
def studentDetail(request, enr):
	if request.user.is_faculty is False:
		return HttpResponseRedirect(reverse('student:dashboard'))

	else:
		Student = get_object_or_404(StudentProfile, enrollment_no=enr)
		school_education = SchoolEducation.objects.filter(student=Student)
		college_education = CollegeEducation.objects.filter(student=Student)
		internship = WorkExperience.objects.filter(student=Student, category="Internship")
		project = WorkExperience.objects.filter(student=Student, category="Project")
		training = WorkExperience.objects.filter(student=Student, category="Training")
		achievement = WorkExperience.objects.filter(student=Student, category="Achievement")
		other = WorkExperience.objects.filter(student=Student, category="Other")
		marksheet = MarkSheet.objects.filter(student=Student)
		if marksheet:
			marksheet = marksheet[0]


		context = {
        	'student' : Student,
			'school_education': school_education,
			'college_education': college_education,
			'internship': internship,
			'project': project,
			'training': training,
			'achievement': achievement,
			'other': other,
			'marksheet': marksheet,
			}

		return render(request, template_name='faculty/student_detail.html', context=context )
