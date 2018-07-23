from django.contrib import admin
from django.conf.urls import include, url
from . import views
urlpatterns = [
    url('', include('users.urls')),
    # url('preferences/', include('users.urls')),
    url('api/dashboard/$', views.index,name="home_page"),
    url('rest-auth/', include('rest_auth.urls')),
    url('rest-auth/registration/', include('rest_auth.registration.urls')),
]