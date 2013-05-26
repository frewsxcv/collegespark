from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'collegespark.views.home', name='home'),
    # url(r'^collegespark/', include('collegespark.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('collegespark.core.urls')),
    url(r'^(?P<school_name>\w+)/book', include('collegespark.book.urls')),
    url(r'^(?P<school_name>\w+)/chat', include('collegespark.chat.urls')),
    url(r'^(?P<school_name>\w+)/discussion', include('collegespark.discussion.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
