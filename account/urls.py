from django.urls import path
from account import views as account_views

app_name = 'account'

urlpatterns = [
    path('register/', account_views.student_register, name='student_register'),
    path('login/', account_views.student_login, name='student_login'),
    path('logout/', account_views.user_logout, name='logout'),
    path('faculty_register', account_views.faculty_register, name='faculty_register'),
    path('faculty_login', account_views.faculty_login, name='faculty_login'),
]
