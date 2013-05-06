from django.shortcuts    import render_to_response
from django.template     import RequestContext
from django.http         import HttpResponseRedirect, HttpResponse
from django.http         import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from forms               import DiscussionForm
from collegespark.discussion.models import Forum, Category
import json
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core import serializers

def paginator_category(request, school_name):
    print "paginator_category"
    if 'page' in request.GET:
        page_num = int(request.GET['page'])
    else:
        page_num = 1

    if 'per_page' in request.GET:
        per_page = int(request.GET['per_page'])
    else:
        per_page = 3

    from_page = (page_num - 1) * per_page
    to_page = page_num * per_page

    categories = Category.objects.all()[from_page:to_page]
    jsonCtx = serializers.serialize('json', categories)
    return HttpResponse(jsonCtx, mimetype='application/json')


def discussion_view(request, school_name):
    categories_count = Category.objects.count()

    ctx = {"categories_count": categories_count}
    return render_to_response(
        'discussion/discussion.html', ctx, context_instance=RequestContext(request))


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
