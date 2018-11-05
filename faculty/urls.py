from django.urls import path
from faculty import views as faculty_views

urlpatterns = [
    path('', faculty_views.index, name='index'),
]
