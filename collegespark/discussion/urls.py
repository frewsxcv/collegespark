from django.conf.urls import patterns, url

urlpatterns = patterns('collegespark.discussion.views',
    url(r'post$', 'post_discussion_view', name='postdiscussion'),
)
