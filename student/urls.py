from django.urls import path
from student import views as student_views

app_name = 'student'

urlpatterns = [
    path('', student_views.dashboard, name='dashboard'),

    path('student_profile_dash_form/', student_views.studentProfileDashView, name='student_profile_dash_form'),
    path('edit-profile/', student_views.edit_profile, name='edit_profile'),
    path('marks/', student_views.createMarkSheetView, name='add_marks'),
    path('basic-details/', student_views.createExtraInfoView, name='basic_details'),
    path('workexperience/', student_views.WorkExperienceView, name='work_experience'),
    path('deleteworkexperience/<int:pk>/', student_views.deleteWorkExperienceView, name='delete_work_experience'),
   # path('school-education/', student_views.schoolEducation, name='school-education'),

    path('school-education/<int:pk>/', student_views.schoolEducation, name='school-education'),
    # path('college-education/', student_views.collegeEducation, name='college-education'),
    path('work-exp/<category>/', student_views.workExperienceDashView, name='work-exp'),
    path('work-exp/', student_views.workExperienceDashView, name='work-exp'),
    path('work-exp/edit/<int:pk>/', student_views.editWorkExperienceDashView, name='editttt'),

    path('college-education/', student_views.collegeEducationDashView, name='college-education'),
    path('college-education/<course>/', student_views.collegeEducationDashView, name='college-education'),

]
