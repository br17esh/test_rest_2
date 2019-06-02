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
from mg_iucaaapp import views2
from dqrreport import views1
from mg_dqrreport import views3
from uploadwise import views4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iucaaapp/', views.summaryList.as_view()),
    path('dqrreport/dqrstats', views1.dqrstatsList.as_view()),
    path('dqrreport/dph', views1.dphList.as_view()),
    path('dqrreport/obsinfo', views1.obsinfoList.as_view()),
    path('dqrreport/housekeeping', views1.housekeepingList.as_view()),
    path('dqrreport/countrate', views1.countrateList.as_view()),
    path('dqrreport/datainteg', views1.dataintegList.as_view()),
    path('dqrreport/datasat', views1.datasatList.as_view()),
    path('dqrreport/noisefrag', views1.noisefragList.as_view()),
    path('dqrreport/pixelprop', views1.pixelpropList.as_view()),
    path('dqrreport/quadprop', views1.quadpropList.as_view()),

    path('mg_iucaaapp/', views2.summaryList.as_view()),

    path('mg_dqrreport/dqrstats', views3.dqrstatsList.as_view()),
    path('mg_dqrreport/dph', views3.dphList.as_view()),
    path('mg_dqrreport/obsinfo', views3.obsinfoList.as_view()),
    path('mg_dqrreport/housekeeping', views3.housekeepingList.as_view()),
    path('mg_dqrreport/countrate', views3.countrateList.as_view()),
    path('mg_dqrreport/datainteg', views3.dataintegList.as_view()),
    path('mg_dqrreport/datasat', views3.datasatList.as_view()),
    path('mg_dqrreport/noisefrag', views3.noisefragList.as_view()),
    path('mg_dqrreport/pixelprop', views3.pixelpropList.as_view()),
    path('mg_dqrreport/quadprop', views3.quadpropList.as_view()),

    path('uploadwise/upobsid', views4.upobsidList.as_view()),

]
