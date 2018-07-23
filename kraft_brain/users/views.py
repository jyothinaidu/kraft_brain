from rest_framework import generics
from .models import Preferences,Favourites,UserAnswers
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status




class UserListCreateView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)






class PreferencesListCreateView(generics.ListCreateAPIView):
    queryset = Preferences.objects.all()
    serializer_class = serializers.PreferencesSerializer


class PreferencesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Preferences.objects.all()
    serializer_class = serializers.PreferencesSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





class FavouritesListCreateView(generics.ListCreateAPIView):
    queryset = Favourites.objects.all()
    serializer_class = serializers.FavouritesSerializer

class FavouritesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favourites.objects.all()
    serializer_class = serializers.FavouritesSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





class UserAnswersListCreateView(generics.ListCreateAPIView):
    queryset =UserAnswers.objects.all()
    serializer_class = serializers.UserAnswersSerializer

class UserAnswersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAnswers.objects.all()
    serializer_class = serializers.UserAnswersSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)