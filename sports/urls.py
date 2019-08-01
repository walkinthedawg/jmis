"""joinsports URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from .views import get_sports, sport_detail, create_or_edit_sport, sports

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', sports, name='sports'),
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^$', get_sports, name='get_sports'),
    url(r'^(?P<pk>\d+)/$', sport_detail, name='sport_detail'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_sport, name='edit_sport')
]
