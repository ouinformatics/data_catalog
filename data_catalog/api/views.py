# Create your views here.
from api import UserResource
from django.http import HttpResponse
import json


def get_api_key(request):
    ur = UserResource()

    #user = ur.obj_get(username=request.user)

    return HttpResponse("API - Key")