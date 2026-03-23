"""
URL configuration for SportsMatches project.

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
from django.urls import path

from page.views import home_view, discover_view
from club.views import club_detail_view, club_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('discover/', discover_view, name='discover'),
    path('admin/', admin.site.urls),
    path('club/', club_detail_view, name='club'),
    path('clubcreate/', club_create_view, name='club_create'),
]
