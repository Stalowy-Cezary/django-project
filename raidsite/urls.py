from django.views.generic import RedirectView

from wings import views
"""raidsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='admin/')),
    path('home/', views.HomeListView.as_view()),
    path('home/<POGGERS>/', views.HomeListView.as_view(), name='home'),
    path('raid/', views.RaidListView.as_view()),
    path('raid/<name>/', views.RaidListView.as_view(), name='raid-detail'),
    #path('spirit-vale/', views.RaidListView.as_view()),
    #path('salvation-pass/', views.RaidListView.as_view()),
    #path('stronghold-of-the-faithful/', views.RaidListView.as_view()),
    #path('bastion-of-the-penitent/', views.RaidListView.as_view()),
]
