__author__ = 'mstacy'
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from django.conf import settings
from tastypie_elasticsearch import resources
#  from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
#from models import Entry


class ESearchResource(resources.ElasticsearchResource):
    class Meta:
        resource_name = 'movie_db'
        es_server = getattr(settings, "ES_INDEX_SERVER", "127.0.0.1:9200")
        es_timeout = 20
        #indices = ["movie_db","twitter"]  # ices = ["twitter"]
        index = resource_name #"movie_db"
        doc_type = None
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
    def determine_format(self, request):
        return "application/json"

class twitterResource(resources.ElasticsearchResource):
    class Meta:
        resource_name = 'twitter'
        es_server = getattr(settings, "ES_INDEX_SERVER", "127.0.0.1:9200")
        es_timeout = 20
        #indices = ["movie_db","twitter"]  # ices = ["twitter"]
        index = resource_name #"movie_db"
        doc_type = None
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
    def determine_format(self, request):
        return "application/json"


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        list_allowed_methods = ['get', 'post']
        fields = ['id', 'username', 'first_name', 'last_name', 'last_login']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = Authorization() ##DjangoAuthorization()

    def determine_format(self, request):
        return "application/json"
    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user=request.user)