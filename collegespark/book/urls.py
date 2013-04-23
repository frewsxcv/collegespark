from django.conf.urls import patterns, url

urlpatterns = patterns('collegespark.book.views',
                       url(r'addbook$', 'add_book_view', name='addbook'),
                       url(r'viewbook/(?P<user_id>\w+)/(?P<book_id>\w+)',
                           'single_book_view', name='singlebook'),
                       url(r'$', 'book_view', name='book'),
                       )
