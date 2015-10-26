"""sapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from accounts.views import ProfileViewSet
from menu.views import MenuViewSet



from rest_framework.routers import DefaultRouter
from accounts.models import Profile

from utils.drf_helpers import ObtainAuthTokenAndProfile, JSONSerializer

router_v1 = DefaultRouter()

router_v1.register(r'menu', MenuViewSet)
router_v1.register(r'profile', ProfileViewSet)

api_urls_v1 = router_v1.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(api_urls_v1)),
    url(r'^api/v1/authenticate/', ObtainAuthTokenAndProfile.as_view()),
]
