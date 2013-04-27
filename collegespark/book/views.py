from django.shortcuts    import render_to_response
from django.template     import RequestContext
from django.http         import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from forms               import BookInfoForm
import json
from django.contrib.auth.decorators import login_required


def book_view(request, school_name):
    print "here"
    ctx = "book view"
    return render_to_response('book/book.html', ctx,
                              context_instance=RequestContext(request))


@login_required(login_url='/')
def add_book_view(request, school_name):
    print "add book view"
    if request.method == 'POST':
        print "post inside"
        addbook_msg = {}
        user = request.user
        school = request.user.school
        ip = request.META.get('REMOTE_ADDR', None)

        book_form_kwargs = {"user": user, "school_name": school,
                            "ip": ip}

        BookForm = BookInfoForm(request.POST, request.FILES,
                                **book_form_kwargs)

        #print BookForm.base_fields
        print request.FILES
        if BookForm.is_valid():
            #print BookForm
            BookForm.save()
            #print BookForm.book.id
            url = "/" + school_name + "/book"
            url = url + "/viewbook/" + str(request.user.id)
            url = url + "/" + str(BookForm.book.id) + "/"
            addbook_msg['redirect_url'] = url
        else:
            print "add book error"
            addbook_msg['errors'] = BookForm.errors

        jsonCtx = json.dumps(addbook_msg)
        return HttpResponse(jsonCtx, mimetype='application/json')

    else:
        bookInfo_form = BookInfoForm()
        ctx = {'bookInfo_form': bookInfo_form}
        return render_to_response('book/addBook.html', ctx,
                                  context_instance=RequestContext(request))


def single_book_view(request, school_name, user_id, book_id):
    ctx = "single book view"
    print "single book view"
    return render_to_response('book/addbookresult.html', ctx,
                              context_instance=RequestContext(request))

