from django.db import models
from django.core.models import School, User


class Book(models.Model):
    def url(self, filename):
        route = "MultimediaData/Books/%s/%s/"%(self.school_name, str(filename))
        return route

    seller = models.ForeignKey('core.User')
    school_name = models.ForeignKey('core.School')
    dpt_name = models.CharField(max_length=40, blank=False)
    class_name = models.CharField(max_length=20, blank=False)
    book_name = models.CharField(max_length=40, blank=False)
    author = models.CharField(max_length=20, blank=False)
    ISBN = models.CharField(max_length=20, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    decription = models.TextField(max_length=300, blank=False)
    condition = models.BooleanField(default=False, blank=False)
    image = models.ImageField(upload_to=url, null=True, blank=False)

    def __unicode__(self):
        return self.book_name
