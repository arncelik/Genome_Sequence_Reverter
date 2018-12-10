"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from genome_functionalities import views as genome_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('', genome_views.home, name='app-home'),
    path('restriction/', genome_views.restrict, name='restriction'),
    path('translation/', genome_views.translate, name='translate'),
    path('transcription/', genome_views.transcribe, name='transcribe'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # normally it searches for template in registration folder therefore we are telling to look at users folder template.
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),  # normally it searches for template in registration folder therefore we are telling to look at users folder template.
    # path('', include('genome_functionalities.urls')),
    path('', include('blog.urls')),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),  # normally it searches for template in registration folder therefore we are telling to look at users folder template.
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),  # normally it searches for template in registration folder therefore we are telling to look at users folder template.
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),  # normally it searches for template in registration folder therefore we are telling to look at users folder template.
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),  # normally it searches for template in registration folder therefore we are telling to look at users folder template.


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # This lets us to be able access the profile images directly on profile.html
