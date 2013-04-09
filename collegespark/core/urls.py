from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('collegespark.core.views',
    url(r'^$', 'index_view', name='index'),
    url(r'^loginValidation/$', 'login_validation')
)