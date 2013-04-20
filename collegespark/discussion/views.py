from django.shortcuts    import render_to_response
from django.template     import RequestContext
from django.http         import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from forms               import PostDiscussionForm


def post_discussion_view(request, school_name):
    return render_to_response(
        'discussion/postDiscussion.html', context_instance=RequestContext(request))
