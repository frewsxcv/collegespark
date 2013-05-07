from django.conf.urls import patterns, url

urlpatterns = patterns('collegespark.book.views',
                       url(r'addbook$', 'add_book_view', name='addbook'),
                       url(r'/(?P<book_id>\w+)/$',
                           'single_book_view', name='single'),
                       url(r'$', 'book_view', name='book'),
                       )
