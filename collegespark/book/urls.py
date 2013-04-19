from django.conf.urls import patterns, url

urlpatterns = patterns('collegespark.book.views',
    url(r'add$', 'add_book_view', name='addbook'),
    url(r'$', 'book_view', name='book'),
)
