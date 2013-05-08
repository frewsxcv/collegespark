from django.db import models
from collegespark.core.models import School, User, Department, Class
import datetime


class Book(models.Model):
    def url(self, filename):
        route = "MultimediaData/Books/%s/%s"%(self.school_name.name, str(filename))
        return route

    seller = models.ForeignKey(User)
    school_name = models.ForeignKey(School)
    isSold = models.BooleanField(default=False, blank=True)
    views = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(default=datetime.datetime.now())
    user_ip = models.GenericIPAddressField(blank=True, null=True)
    dpt_name = models.CharField(max_length=40, blank=False)
    class_name = models.CharField(max_length=20, blank=False)
    book_name = models.CharField(max_length=40, blank=False)
    author = models.CharField(max_length=20, blank=True)
    ISBN = models.CharField(max_length=20, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    description = models.TextField(max_length=300, blank=False)
    condition = models.BooleanField(default=False, blank=False)
    image = models.ImageField(upload_to=url, null=True, blank=True)

    def __unicode__(self):
        return self.book_name
