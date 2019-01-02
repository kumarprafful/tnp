from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from student.models import StudentProfile
import json
from django.core import serializers

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
					if int(i.admission_year) == int(j):
						year_filter += StudentProfile.objects.filter(enrollment_no = i.enrollment_no).values()
						break
			else:
				year_filter += StudentProfile.objects.filter(enrollment_no = i.enrollment_no).values()



		data = {
			'filtered_students': year_filter
		}

		return JsonResponse(data, safe=False)
