"""CDX2016 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include, patterns
from django.contrib import admin
from Citadel.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^register/continue/', register),
    url(r'^register/', registerFirst),
    url(r'^login/', usrlogin),
    url(r'^profile/', user_profile),
    url(r'^logout/', user_logout),
    url(r'^messages/add-message/', addMessage),
    url(r'^messages/', messageView),
    url(r'^citizens/make/', makeCitizen),
    url(r'^citizens/(?P<citid>[0-9]+)/edit/', editCitizen),
    url(r'^citizens/(?P<citid>[0-9]+)/delete/', deleteCitizens),
    url(r'^citizens/', seeCitizens),
]

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)
