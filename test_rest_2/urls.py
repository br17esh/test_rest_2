"""test_rest_2 URL Configuration

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
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from iucaaapp import views
from dqrreport import views1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iucaaapp/', views.summaryList.as_view()),
    path('dqrreport/dqrstats', views1.dqrstatsList.as_view()),
    path('dqrreport/dph', views1.dphList.as_view()),
    path('dqrreport/obsinfo', views1.obsinfoList.as_view()),
    path('dqrreport/housekeeping', views1.housekeepingList.as_view()),
    path('dqrreport/countrate', views1.countrateList.as_view()),
]
