from django.urls import path
from faculty import views as faculty_views

app_name = 'faculty'

urlpatterns = [
    path('', faculty_views.dashboard, name='dashboard'),
]
