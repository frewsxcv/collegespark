from django.conf.urls import patterns, url

urlpatterns = patterns('collegespark.discussion.views',
    url(r'post$', 'discussion_form_view', name='postdiscussion'),
)
