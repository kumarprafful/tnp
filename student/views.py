from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from student.models import StudentProfile
from student.forms import StudentProfileForm

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
