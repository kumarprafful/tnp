from django.contrib import admin
from django.urls import path, include, reverse, reverse_lazy
from account import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/', include('api.endpoints')),
    path('api/auth', include('knox.urls')),
    path('account/', include('account.urls')),
    path('student/', include('student.urls')),
    path('faculty/', include('faculty.urls')),
    path('activate/<uidb64>[0-9A-Za-z_\-]+/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20}', account_views.activate, name='activate'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
