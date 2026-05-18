"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homeview),
    path('about/', views.aboutview),
    path('python/', views.pythonview),
    path('java/', views.javaview),
    path('django/', views.djangoview),
    path('mern/', views.mernview),
    path('photos/', views.photosview),
    path('videos/', views.videosview),
    path('latestnews/', views.latestnewsview),
    path('parentreg/', views.parentregview),
    path('contact/', views.contactview),
    path('thanks/', views.thanksview),
    path('delete/<int:id>/', views.deleteview),
    path('update/<int:id>/', views.updateview),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logoutview, name='logout'),
    path('thanks/', views.thanksview, name='thanks'),
    path('register/', views.signupview),

]
