from django.conf.urls import patterns, url

urlpatterns = patterns('collegespark.discussion.views',
    url(r'/paginator/(?P<page_name>\w+)$', 'paginator_data'),
    url(r'/post$', 'discussion_form_view', name='postdiscussion'),
    url(r'/departments$', 'category_view', name='category'),
    url(r'/(?P<post_id>\d+)/(?P<post_type>[a-zA-Z0-9-/]+)$', 'post_body_view', name='full_post'),
    url(r'/(?P<department>[a-zA-Z-/]+)$', 'topic_view', name='topic'),
    url(r'/(?P<department>[a-zA-Z-/]+)/(?P<post_class>[a-zA-Z0-9-/]+)$', 'post_view', name='post'),
    url(r'$', 'discussion_view', name='discussion'),
)
