from django.shortcuts import render
from rest_framework.reverse import reverse
# Create your views here.
def index(request,format=None):
    final_output = {
        'Users List': reverse('user_list', request=request, format=format),
        'Users Create': reverse('user_list_create', request=request, format=format),
        'Answers List': reverse('answers_list', request=request, format=format),
        'Answers Create': reverse('answers_list_create', request=request, format=format),
        'Preference List': reverse('preferences_list', request=request, format=format),
        'Preferences Create': reverse('preferences_list_create', request=request, format=format),
        'Favourites List': reverse('preferences_list', request=request, format=format),
        'Favourites Create': reverse('preferences_list_create', request=request, format=format),

    }


    return render(request, 'rest_framework/dashboard.html',{'final_output':final_output})