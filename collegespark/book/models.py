from django.db import models


class book(models.Model):
    def url(self, filename):
        route = "MultimediaData/Books/%s/%s"%(self.name, str(filename))
        return route

    school_name = models.CharField(max_length=40)
    dpt_name = models.CharField(max_length=40)
    class_name = models.CharField(max_length=20)
    book_name = models.CharField(max_length=40)
    author = models.CharField(max_length=20)
    ISBN = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    decription = models.TextField(max_length=300)
    condition = models.BooleanField(default=False)
    image = models.ImageField(upload_to=url, null=True, blank=True)

    def __unicode__(self):
        return self.name
