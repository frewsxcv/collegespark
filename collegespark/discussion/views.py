from django.shortcuts    import render_to_response
from django.template     import RequestContext
from django.http         import HttpResponseRedirect, HttpResponse
from django.http         import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from forms               import DiscussionForm
from collegespark.discussion.models import Forum, Category, Topic, Post
import json
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core import serializers


def discussion_view(request, school_name):
    category_count = Category.objects.count()

    ctx = {"category_count": category_count}
    return render_to_response(
        'discussion/discussion.html', ctx, context_instance=RequestContext(request))


def category_view(request, school_name):
    category_count = Category.objects.count()

    ctx = {"category_count": category_count}

    return render_to_response(
        'discussion/category.html', ctx, context_instance=RequestContext(request))


def topic_view(request, school_name, department):
    department_name = convert_from_dash_to_space(
        check_for_forward_slash(department))

    print department_name
    topic_count = get_topic_count(school_name, department_name)

    ctx = {
        "topic_name": department_name,
        "topic_count": topic_count}
    print ctx
    return render_to_response(
        'discussion/topic.html', ctx, context_instance=RequestContext(request))


def post_view(request, school_name, department, post_class):
    department_name = convert_from_dash_to_space(department)
    class_name = convert_from_dash_to_space(
        check_for_forward_slash(post_class))
    post_count = get_post_count(school_name, department_name, class_name)

    ctx = {
        "topic_name": department_name,
        "post_name": class_name,
        "post_count": post_count
    }
    print ctx
    return render_to_response(
        'discussion/post.html', ctx, context_instance=RequestContext(request))


def discussion_form_view(request, school_name):
    form_msg = {}

    if request.method == 'POST':
        user = request.user
        forum = Forum.objects.get(school=request.user.school)
        ip = request.META.get('REMOTE_ADDR', None)

        post_form_kwargs = {"user": user, "forum": forum, "ip": ip}

        discussionForm = DiscussionForm(request.POST, **post_form_kwargs)

        if discussionForm.is_valid():
            print discussionForm.cleaned_data
            discussionForm.save()

            form_msg['redirect_url'] = "something"
        else:
            print discussionForm.errors
            form_msg['errors'] = discussionForm.errors

        jsonCtx = json.dumps(form_msg)
        return HttpResponse(jsonCtx, mimetype='application/json')

    else:
        discussionForm = DiscussionForm()

        ctx = {'discussionForm': discussionForm}
        return render_to_response(
            'discussion/postDiscussion.html', ctx, context_instance=RequestContext(request))


def paginator_data(request, page_name, school_name):
    print "paginator_category"
    request_get = request.GET

    if 'page' in request.GET:
        page_num = int(request.GET['page'])
    else:
        page_num = 1

    if 'per_page' in request.GET:
        per_page = int(request.GET['per_page'])
    else:
        per_page = 3

    limit_from = (page_num - 1) * per_page
    limit_to = page_num * per_page
    print page_name
    if page_name == "topic":
        data = get_topic(
            school_name, request.GET['topic_name'], limit_from, limit_to)
    elif page_name == "post":
        data = get_post(
            school_name, request_get['topic_name'],
            request_get['post_name'],
            limit_from, limit_to)
    else:
        data = Category.objects.all()[limit_from:limit_to]

    jsonCtx = serializers.serialize('json', data)
    return HttpResponse(jsonCtx, mimetype='application/json')


def get_topic_count(school_name, department_name):
    return Topic.objects.filter(
        category__name__iexact=department_name,
        category__forum__school__short_name__iexact=school_name).count()


def get_topic(school_name, department_name, limit_from, limit_to):
    return Topic.objects.filter(
        category__name__iexact=department_name,
        category__forum__school__short_name__iexact=school_name)[
            limit_from:limit_to]


def get_post_count(school_name, department_name, class_name):
    return Post.objects.filter(
        topic__name__iexact=class_name,
        topic__category__name__iexact=department_name,
        topic__category__forum__school__short_name__iexact=school_name).count()


def get_post(school_name, department_name, class_name, limit_from, limit_to):
    return Post.objects.filter(
        topic__name__iexact=class_name,
        topic__category__name__iexact=department_name,
        topic__category__forum__school__short_name__iexact=school_name)[
            limit_from:limit_to]


def convert_from_dash_to_space(name):
    return name.replace("-", " ")


def check_for_forward_slash(name):
    if name[-1:] == "/":
        return name[:-1]
    else:
        return name
