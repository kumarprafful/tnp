from django.urls import path
from .views import index, student_register, student_login, user_logout

urlpatterns = [
    path('', index, name='index'),
    path('register/', student_register, name='student_register'),
    path('login/', student_login, name='student_login'),
    path('logout/', user_logout, name='logout'),

]
