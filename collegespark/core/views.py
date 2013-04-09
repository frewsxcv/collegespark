from django.shortcuts    import render_to_response
from django.template     import RequestContext
from django.http         import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from forms               import LoginForm, SignUpForm
from django.contrib.auth.models import User


def index_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    else:
        login_form  = LoginForm()
        signup_from = SignUpForm()

    ctx = {'login_form': login_form,
           'signup_from': signup_from}

    return render_to_response('front.html', ctx,
           context_instance=RequestContext(request))


def login_validation(request):
    login_msg = ""
    login_form = LoginForm(request.POST)

    if login_form.is_valid():
        email    = login_form.cleaned_data['email']
        password = login_form.cleaned_data['password']

        user_auth = authenticate_user(email, password)
        if user_auth is not None and user_auth.is_active:
            login(request, user_auth)
            return HttpResponseRedirect('/home')
        else:
            login_msg = "email and password is wrong"

    return HttpResponse(login_msg, mimetype='application/json')


def signup_validation(request):
    signup_msg  = {}
    signup_from = SignUpForm(request.POST)

    if signup_from.is_valid():
        email    = signup_from.cleaned_data['email']
        school   = signup_from.cleaned_data['school']
        password = signup_from.cleaned_data['password']
        re_enter_password = signup_from.cleaned_data['re_enter_password']

    if is_user_exist(email):
        signup_msg['email'] = "This email address has been used"

    if password != re_enter_password:
        signup_msg['password'] = "password are same"

    if not signup_msg:
        signup_user({'email': email,
                     'school': school,
                     'password': password})

        user_auth = authenticate_user(email, password)
        if user_auth is not None and user_auth.is_active:
            login(request, user_auth)
            return HttpResponseRedirect('/home')
        else:
            #TODO: I dont know what to do here
            print "TODO: function signup_user"

        return HttpResponseRedirect('/home')
    else:
        return HttpResponse(signup_msg, mimetype='application/json')


def signup_user(user_info):
    email    = user_info['email']
    school   = user_info['school']
    password = user_info['password']
    username = email.split('@')[0]

    user = User.objects.create_user(username, email, password)
    user.school = school
    user.save()


def is_user_exist(email):
    if User.objects.filter(email=email).exists():
        return True

    return False


def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            return user

    except User.DoesNotExist:
        return None
