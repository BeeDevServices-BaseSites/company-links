from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import *


def index(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in")
        return render(request, 'logReg.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        request.session['role']= user.role
        role = request.session['role']
        context = {
            'user': user,
            'role': role
        }
    return render(request, 'index.html', context)

def logout(request):
    request.session.clear()
    messages.error(request, 'You have ben logged out')
    return redirect('/')