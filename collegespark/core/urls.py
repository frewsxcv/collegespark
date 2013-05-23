from django.conf.urls import patterns, url

urlpatterns = patterns(
    'collegespark.core.views',
    url(r'^$', 'index_view', name='index'),
    url(r'^logout$', 'logout_view', name='logout'),
    url(r'^login/validation$', 'login_validation'),
    url(r'^signup/validation$', 'signup_validation'),
    url(r'^email/validation$', 'email_validation'),
    url(r'^(?P<school_name>\w+)/?$', 'dashboard_view', name='dashboard')
)
