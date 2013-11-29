# Create your views here.
from api import UserResource
from django.http import HttpResponse
import json


def get_api_key(request):
    ur = UserResource()

    #user = ur.obj_get(username=request.user)

    return HttpResponse("API - Key")

# Create your views here.
from django.http import HttpResponse #, HttpResponseForbidden #,HttpResponseRedirect
from django.contrib.auth.models import User
#from django.db import models
#from tastypie.models import create_api_key
from tastypie.models import ApiKey
#from django.contrib.auth.decorators import login_required

def generate_api(request, username, password, **kwargs):
    '''
        Function Resets or creates new API key for authenticated users
        or provide username and password
    '''

    if request.user.is_authenticated():
        api_key = reset_or_createAPI(request.user)
    else:
        print username, password
        if credentialCheck(username,password):
            user = User.objects.get(username=username)
            api_key = reset_or_createAPI(user)
        else:
            return HttpResponse("Forbidden()")
    return HttpResponse(api_key)

def credentialCheck(username,password):

    # Check if user exists
    try:
        user = User.objects.get(username=username)
    except (User.DoesNotExist, User.MultipleObjectsReturned):
        return False #HttpResponseForbidden()

    # Check if user has correct password
    if not user.check_password(password):
        return False #HttpResponseForbidden()
    return True

def reset_or_createAPI(user):
    try:
        api_key = ApiKey.objects.get(user=user)
        api_key.key = None
        api_key.save()
    except ApiKey.DoesNotExist:
        api_key = ApiKey.objects.create(user=user)
    return api_key.key

#@login_required()
def test_auth(request):
    return HttpResponse("Success - Auth")
