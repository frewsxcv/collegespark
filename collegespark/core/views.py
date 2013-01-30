from django.shortcuts import render_to_response
from django.template import RequestContext


def front(request):
    return render_to_response('front.html', context_instance=RequestContext(request))
