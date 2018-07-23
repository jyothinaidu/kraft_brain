from rest_framework import serializers
from . import models
from django.conf import settings

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
# from firebase_admin import auth
from django.contrib.auth import authenticate, user_logged_in
import requests
import json
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler
import pyrebase
import datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import AbstractUser
from firebase import firebase as post_firebase
from rest_framework.validators import UniqueValidator
import base64
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from base import utils as base_utils
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.decorators import api_view,renderer_classes
from django.views.decorators.csrf import csrf_protect
from .models import Preferences,Favourites,UserAnswers,CustomUser


class PreferencesSerializer(serializers.ModelSerializer):
    favourites = serializers.PrimaryKeyRelatedField(queryset=Favourites.objects.all())

    class Meta:
        model = Preferences
        fields = ('id','type','name','favourites')


class UserAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswers
        fields = ('id','answer_activity_id','answer_group_id','answer_id','answer_source','answer_value','choce_id',
                  'language_id','question_id','status','weight_value')


class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = ('id','name','description')

class UserSerializer(serializers.ModelSerializer):
    preferences = serializers.PrimaryKeyRelatedField(queryset=Preferences.objects.all())
    favourites = serializers.PrimaryKeyRelatedField(queryset=Favourites.objects.all())
    answers = serializers.PrimaryKeyRelatedField(queryset=UserAnswers.objects.all())

    class Meta:
        model = CustomUser
        fields = ('id','username', 'email', 'password', 'first_name', 'last_name', 'site_id',
                  'news_letter','nickname','language_id','registration_source','registration_activity_id',
                  'address2','address1','gender','phone2','phone1','dob','is_staff','is_active','answers',
                  'preferences','favourites')

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_password(self, value):
        if len(value) < getattr(settings, 'PASSWORD_MIN_LENGTH', 8):
            raise serializers.ValidationError(
                "Password should be atleast %s characters long." % getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
            )
        return value

    def validate_password_2(self, value):
        data = self.get_initial()
        password = data.get('password')
        if password != value:
            raise serializers.ValidationError("Passwords doesn't match.")
        return value

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value


