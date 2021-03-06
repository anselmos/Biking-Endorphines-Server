"""bikingendorphines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from api import views

#pylint: disable=invalid-name
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/user/$', views.UserList.as_view()),
    url(r'^api/user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api/badge/(?P<pk>[0-9]+)/$', views.UserBadgeList.as_view()),
    url(r'^api/point/$', views.PointView.as_view()),
    url(r'^api/points/$', views.PointList.as_view()),
    url(r'^api/file/$', views.FileUploadView.as_view()),
    url(r'^docs/', include_docs_urls(title='API Documentation')),
]
