from django.shortcuts    import render_to_response
from django.template     import RequestContext
from django.http         import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from forms               import BookInfoForm
import json
from django.contrib.auth.decorators import login_required
from collegespark.book.models import Book
from models import User


@login_required(login_url='/')
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
        ctx = {}
        user = request.user
        school = request.user.school
        ip = request.META.get('REMOTE_ADDR', None)

        book_form_kwargs = {"user": user, "school_name": school,
                            "ip": ip}

        BookForm = BookInfoForm(request.POST, request.FILES,
                                **book_form_kwargs)

        print request.FILES
        if BookForm.is_valid():
            BookForm.save()
            url = "/" + school_name + "/book"
            url = url + "/"
            url = url + str(BookForm.book.id) + "/"
            ctx['result'] = 'success'
            ctx['addbookURL'] = url
        else:
            print "add book error"
            ctx['result'] = BookForm.errors
            ctx['addbookURL'] = '/' + school_name + "/book/addbook"

        return render_to_response('book/addbookresult.html', ctx,
                                  context_instance=RequestContext(request))

    else:
        bookInfo_form = BookInfoForm()
        ctx = {'bookInfo_form': bookInfo_form}
        return render_to_response('book/addBook.html', ctx,
                                  context_instance=RequestContext(request))

@login_required(login_url='/')
def single_book_view(request, school_name, book_id):
    ctx = {}
    print "single book view"
    book = Book.objects.get(id=book_id)
    ctx['book'] = book
    ctx['school'] = school_name
    return render_to_response('book/bookview.html', ctx,
                              context_instance=RequestContext(request))
