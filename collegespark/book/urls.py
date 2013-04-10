from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('collegespark.book.views',
    url(r'^addBook/$', 'add_book_view', name='addBook'),
)