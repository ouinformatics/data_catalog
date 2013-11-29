__author__ = 'mstacy'
from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api import ESearchResource, UserResource, twitterResource


v1_api = Api(api_name='v1')
v1_api.register(ESearchResource())
v1_api.register(UserResource())
v1_api.register(twitterResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auth.views.home', name='home'),
    #url(r'^generate_api/',include('myapp.urls')),
    #url(r'testauth/', 'myapp.views.test_auth'),
    #url(r'generate_api/([a-zA-Z0-9 .!@#$%^&*]{0,50})/([a-zA-Z0-9 .!@#$%^&*]{0,50})', 'myapp.views.generate_api'),
    #url(r'getapi/([a-zA-Z0-9 .!@#$%^&*]{0,50})/([a-zA-Z0-9 .!@#$%^&*]{0,50})', GetApiKeyView.as_view()),
    #url(r'getapi/', GetApiKeyView.as_view()),
    #url(r'^blog/', include('myapp.urls')),
    url(r'api/', include(v1_api.urls)),
    url(r'apikey/','api.views.get_api_key'),
    url(r'generate_api/([a-zA-Z0-9 .!@#$%^&*]{0,50})/([a-zA-Z0-9 .!@#$%^&*]{0,50})', 'api.views.generate_api'),
    #url(r'api1/', include(v1_api1.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
