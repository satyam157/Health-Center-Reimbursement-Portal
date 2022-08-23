"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from django.views.generic.base import TemplateView  # new
from . import views
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_views

from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^user/static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("user/", include("user.urls")),
    path("/", user_views.UploadView.as_view(), name="fileupload"),
]
