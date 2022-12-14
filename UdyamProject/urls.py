"""UdyamProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from UdyamProject import views
from urllib.parse import urldefrag
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login', TemplateView.as_view(template_name='login.html'), name='login'),
    path('signup', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('accounts/', include('allauth.urls')),
    path('postlogin', views.handlelogin),
    path('postsignup', views.handleSignUp),
    path('logout', views.handlelogout),
    path('accounts/profile', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('', include('social_django.urls', namespace='social'))
]
