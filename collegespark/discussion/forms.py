from django import forms
from collegespark.discussion.models import Forum, Category, Topic, Post


class DiscussionForm(forms.Form):
    department = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-department',
               'placeholder': 'Please enter the department name ...'}))

    class_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-class_name',
               'placeholder': 'Please enter the class ...'}))

    post_topic = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-xxlarge input-post-topic',
               'placeholder': 'Please enter the topic ...'}))

    post_body = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'post-body',
               'placeholder': 'Please enter the topic description ...'}))

    def __init__(self, *args, **kwargs):
        self.user     = kwargs.pop('user', None)
        self.forum    = kwargs.pop('forum', None)
        self.category = None
        self.topic    = None
        self.post     = None
        self.ip       = kwargs.pop('ip', None)
        super(DiscussionForm, self).__init__(*args, **kwargs)

    def save(self):
        department = self.cleaned_data['department']
        class_name = self.cleaned_data['class_name']
        post_topic = self.cleaned_data['post_topic']
        post_body  = self.cleaned_data['post_body']

        if not self.is_department_exists(department):
            self.save_category(department)
        else:
            self.category = Category.objects.get(
                forum=self.forum,
                name=department)

        if not self.is_topic_exists(class_name):
            self.save_topic(class_name)
        else:
            self.topic = Topic.objects.get(
                category=self.category,
                name=class_name)

        self.post = Post(
            topic=self.topic,
            created_by=self.user,
            post_topic=post_topic,
            post_body=post_body,
            user_ip=self.ip)

        self.post.save()
        self.topic.post_count += 1

    def clean(self):
        return self.cleaned_data

    def is_department_exists(self, department):
        return Category.objects.filter(forum=self.forum, name=department).exists()

    def is_topic_exists(self, topic):
        return Topic.objects.filter(category=self.category, name=topic).exists()

    def save_category(self, department):
        self.category = Category(
            forum=self.forum,
            name=department,
            created_by=self.user)

        self.category.save()

    def save_topic(self, class_name):
        self.topic = Topic(
            category=self.category,
            name=class_name,
            created_by=self.user)

        self.topic.save()
        self.category.topic_count += 1
