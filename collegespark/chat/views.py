from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def chat(request, school_name):
    data = {'school_name': school_name}
    return render(request, 'chat/chat.html', data)
