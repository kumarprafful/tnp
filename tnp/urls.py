from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/', include('api.endpoints')),
    path('account/', include('account.urls')),
    path('student/', include('student.urls')),
    path('faculty', include('faculty.urls')),
]
