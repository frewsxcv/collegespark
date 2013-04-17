from django.shortcuts    import render_to_response
from django.template     import RequestContext
from django.http         import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from forms               import BookInfoForm
from django.contrib.auth.models import User


def book_view(request, school_name):
    print "book view"
    return render_to_response(
        'book/book.html', context_instance=RequestContext(request))

#@login_required
def add_book_view(request, school_name):
    print "-------test -----"
    if request.user.is_authenticated():
        bookInfo_form = BookInfoForm()
    else:
        print "out"
        return HttpResponseRedirect('/')

    ctx = {'bookInfo_form': bookInfo_form}

    return render_to_response('book/addbook.html', ctx, context_instance=RequestContext(request))

'''
def add_Book_toDB_view(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = BookInfoForm(request.POST, request.FILES)
            if form.is_valid():
                school_name = form.cleaned_data['school_name']
                dpt_name = form.cleaned_data['dpt_name']
                class_name = form.cleaned_data['class_name'] 
'''
