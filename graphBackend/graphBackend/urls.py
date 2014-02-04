from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from tastypie.api import Api

from api.rdfResource import PersonResource



api = Api(api_name='v01')
api.register(PersonResource())


from api.neoResource import EntryResource

entry_resource = EntryResource()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'graphBackend.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),


                       (r'^entry/', include(entry_resource.urls)),
)

urlpatterns = urlpatterns + api.urls
