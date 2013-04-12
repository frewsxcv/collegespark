from django.shortcuts               import render_to_response
from django.template                import RequestContext
from django.http                    import HttpResponseRedirect, HttpResponse
from django.contrib.auth            import login, logout, authenticate
from forms                          import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from models                         import User, School
import json


def index_view(request):
    if request.user.is_authenticated():
        print "whyyyyyyyyyyyyyy"
        school_url = '/{}'.format(request.user.school.name)
        return HttpResponseRedirect(school_url)
    else:
        login_form  = LoginForm()
        signup_form = SignUpForm()

    ctx = {'login_form': login_form,
           'signup_form': signup_form}

    return render_to_response(
        'core/index.html', ctx, context_instance=RequestContext(request))


def dashboard_view(request, school_name):
    print school_name
    return render_to_response(
        'core/home.html', context_instance=RequestContext(request))


def login_validation(request):
    print "=========================="
    next       = ""
    login_msg  = {}
    login_form = LoginForm(request.POST)

    if 'next' in request.GET:
        next = request.GET['next']

    if login_form.is_valid():
        email    = request.POST['email_login']
        password = request.POST['password_login']
        user_auth = authenticate(username=email, password=password)

        if user_auth is not None and user_auth.is_active:
            login(request, user_auth)
            if next != "":
                login_msg['redirect_url'] = next
            else:
                login_msg['redirect_url'] = '/{}'.format(request.user.school.name)
        else:
            login_msg['error'] = "email and password is wrong"

    else:
        login_msg['error'] = "something went wrong!"

    jsonCtx = json.dumps(login_msg)
    return HttpResponse(jsonCtx, mimetype='application/json')


def signup_validation(request):
    signup_msg  = {}
    signup_form = SignUpForm(request.POST)

    if signup_form.is_valid():
        email    = request.POST['email']
        school   = request.POST['school']
        password = request.POST['password']
        re_enter_password = request.POST['re_enter_password']

    if is_user_exist(email):
        signup_msg['email'] = "This email address has been used"

    if password != re_enter_password:
        signup_msg['password'] = "password and re-enter password are same"

    if not signup_msg:
        signup_user({'email': email,
                     'school': school,
                     'password': password})

        user_auth = authenticate(username=email, password=password)
        if user_auth is not None and user_auth.is_active:
            login(request, user_auth)
            school_url = '/{}'.format(school)
            return HttpResponseRedirect(school_url)

        else:
            #TODO: I dont know what to do here
            print "TODO: function signup_user"
    else:
        return HttpResponse(signup_msg, mimetype='application/json')


def email_validation(request):
    email = request.POST['email_signup']
    ctx = is_user_exist(email)

    jsonCtx = json.dumps(ctx)
    return HttpResponse(jsonCtx, mimetype='application/json')


def logout_view(request):
    print "**************"
    logout(request)
    return HttpResponseRedirect('/')


def signup_user(user_info):
    email    = user_info['email']
    school   = user_info['school']
    password = user_info['password']
    username = email.split('@')[0]

    user = User.objects.create_user(email, username=username, school=school, password=password)


def is_user_exist(email):
    return User.objects.filter(email=email).exists()

def get_user_schoolname(id):
    school = School.objects.get(id=id)
    return school.name
