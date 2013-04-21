from django.shortcuts    import render_to_response
from django.template     import RequestContext
from django.http         import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from forms               import DiscussionForm
from collegespark.discussion.models import Forum
import json


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
