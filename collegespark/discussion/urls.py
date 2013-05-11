from django.conf.urls import patterns, url

urlpatterns = patterns('collegespark.discussion.views',
    url(r'/category$', 'paginator_category'),
    url(r'/post$', 'discussion_form_view', name='postdiscussion'),
    url(r'/departments$', 'category_view', name='category'),
    url(r'$', 'discussion_view', name='discussion'),
)
