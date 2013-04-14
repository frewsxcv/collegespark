from django.conf.urls import patterns, url

urlpatterns = patterns('collegespark.book.views',
    url(r'^(?P<school_name>\w+)/addbook$', 'add_book_view', name='addbook'),
)