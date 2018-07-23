from django.contrib import admin
from django.conf.urls import include, url

from . import views
from .views import PreferencesListCreateView,FavouritesListCreateView,FavouritesDetailView,PreferencesDetailView,\
    UserDetailView,UserAnswersListCreateView,UserAnswersDetailView

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Kraft-Brain Users API')
urlpatterns = [
    url(r'swagger/$', schema_view),
    url('users/$', views.UserListCreateView.as_view(),name="user_list"),
    url('users/create/$', views.UserListCreateView.as_view(),name="user_list_create"),
    url('users/detail/(?P<pk>[0-9]+)/$', UserDetailView.as_view(),name="user_list_indi"),
    url('users/update/(?P<pk>[0-9]+)/$',UserDetailView.as_view(),name="user_list_update"),
    url('users/delete/(?P<pk>[0-9]+)/$',UserDetailView.as_view(),name="user_list_delete"),

    #

    url('users/preferences/$', PreferencesListCreateView.as_view(),name="preferences_list"),
    url('users/preferences/create/$',PreferencesListCreateView.as_view(),name="preferences_list_create"),
    url('users/preferences/detail/(?P<pk>[0-9]+)/$',PreferencesDetailView.as_view(),name="preferences_list_indi"),
    url('users/preferences/update/(?P<pk>[0-9]+)/$',PreferencesDetailView.as_view(),name="preferences_list_update"),
    url('users/preferences/delete/(?P<pk>[0-9]+)/$',PreferencesDetailView.as_view(),name="preferences_list_delete"),


    url('users/preferences/favourites/$', FavouritesListCreateView.as_view(),name="favourites_list"),
    url('users/preferences/favourites/create/$',FavouritesListCreateView.as_view(),name="favourites_list_create"),
    url('users/preferences/favourites/detail/(?P<pk>[0-9]+)/$',FavouritesDetailView.as_view(),name="favourites_list_indi"),
    url('users/preferences/favourites/update/(?P<pk>[0-9]+)/$',FavouritesDetailView.as_view(),name="favourites_list_update"),
    url('users/preferences/favourites/delete/(?P<pk>[0-9]+)/$',FavouritesDetailView.as_view(),name="favourites_list_delete"),


    url('users/answers/$', UserAnswersListCreateView.as_view(),name="answers_list"),
    url('users/answers/create/$',UserAnswersListCreateView.as_view(),name="answers_list_create"),
    url('users/answers/detail/(?P<pk>[0-9]+)/$',UserAnswersDetailView.as_view(),name="answers_list_indi"),
    url('users/answers/update/(?P<pk>[0-9]+)/$',UserAnswersDetailView.as_view(),name="answers_list_update"),
    url('users/answers/delete/(?P<pk>[0-9]+)/$',UserAnswersDetailView.as_view(),name="answers_list_delete"),

]

