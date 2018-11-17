from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from account.models import StudentProfile

# Create your views here.
@login_required(login_url=reverse_lazy('account:faculty_login'))
def dashboard(request):
    if request.user.is_faculty is False:
        return HttpResponseRedirect(reverse('student:dashboard'))
    else:
    	Students = StudentProfile.objects.all()
    	return render(request, template_name='faculty/faculty_dashboard.html', context = {'Students' : Students })
