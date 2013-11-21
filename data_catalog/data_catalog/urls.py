from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#
#from django.conf.urls import patterns, include, url
#from tastypie.api import Api
#from api.api import EntryResource, ESearchResource, UserResource

#  entry_resource = EntryResource()

#  v1_api = Api(api_name='v1')
#  v1_api.register(ESearchResource())
#  v1_api.register(UserResource())
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'data_catalog.views.home', name='home'),
    url(r'^metadata/', include('api.urls')),
    #'api.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
