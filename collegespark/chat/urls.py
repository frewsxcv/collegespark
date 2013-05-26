from django.conf.urls import patterns, url

urlpatterns = patterns(
    'collegespark.chat.views',
    url(r'$', 'chat', name='chat'),
    #url(r'addbook$', 'add_book_view', name='addbook'),
    #url(r'/(?P<book_id>\w+)/$', 'single_book_view', name='single'),
)
