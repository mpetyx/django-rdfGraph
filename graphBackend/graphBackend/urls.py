from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from tastypie.api import Api

from api.rdfResource import PersonResource

api = Api(api_name='v01')
api.register(PersonResource())

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'graphBackend.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = urlpatterns + api.urls
