from django.contrib import admin
from django.urls import path, include
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/', include('api.endpoints')),
    path('api/auth', include('knox.urls')),
    path('account/', include('account.urls')),
    path('student/', include('student.urls')),
    path('faculty/', include('faculty.urls')),
    path('activate/<uidb64>[0-9A-Za-z_\-]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}', account_views.activate, name='activate'),
]
