'''
Each School has a Fourm, then each Fourm has Categories which is the
departments of the school. Each Category has Topic which is the class
of that department. At the end each Topic has post.
'''
from django.db import models
from collegespark.core.models import User, School
import datetime


class Forum(models.Model):
    name   = models.CharField(max_length=100)
    school = models.ForeignKey(School)

    def __unicode__(self):
        return self.name


#This is the department of the school
class Category(models.Model):
    forum       = models.ForeignKey(Forum)
    name        = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, default='')
    created     = models.DateTimeField(default=datetime.datetime.now())
    updated     = models.DateTimeField(null=True)
    created_by  = models.ForeignKey(User)
    views       = models.IntegerField(blank=True, default=0)
    topic_count = models.IntegerField(blank=True, default=0)
    last_post   = models.ForeignKey('Post', blank=True, null=True)

    def __unicode__(self):
        return self.name

    @property
    def reply_count(self):
        return self.post_count - 1


#This is the class of the school
class Topic(models.Model):
    category    = models.ForeignKey(Category)
    name        = models.CharField(max_length=255)
    created     = models.DateTimeField(default=datetime.datetime.now())
    updated     = models.DateTimeField(null=True)
    created_by  = models.ForeignKey(User)
    views       = models.IntegerField(blank=True, default=0)
    subscribers = models.ManyToManyField(User, related_name='subscribers', blank=True)
    post_count  = models.IntegerField(blank=True, default=0)
    last_post   = models.ForeignKey('Post', related_name='last_post', blank=True, null=True)

    def __unicode__(self):
        return self.name

    @property
    def reply_count(self):
        return self.post_count - 1


class Post(models.Model):
    topic      = models.ForeignKey(Topic)
    created_by = models.ForeignKey(User)
    created    = models.DateTimeField(default=datetime.datetime.now())
    updated    = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(User, related_name='updated_by', blank=True, null=True)
    post_topic = models.TextField()
    post_body  = models.TextField()
    user_ip    = models.GenericIPAddressField(blank=True, null=True)
    #TODO add reply_count
    '''TODO add for preformance (denormilize)
        topic_name,
        category_name
    '''


class Reply(models.Model):
    post          = models.ForeignKey(Post)
    created_by    = models.ForeignKey(User)
    created       = models.DateTimeField(default=datetime.datetime.now())
    updated       = models.DateTimeField(null=True)
    reply_body    = models.TextField()
    user_ip       = models.GenericIPAddressField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, default=0)


class ReplyComment(models.Model):
    reply        = models.ForeignKey(Reply)
    created_by   = models.ForeignKey(User)
    created      = models.DateTimeField(default=datetime.datetime.now())
    reply_body   = models.TextField()
    comment_body = models.TextField()
    user_ip      = models.GenericIPAddressField(blank=True, null=True)
