from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.forms import *
from user.models import *
from core.models import *


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

def createPolicy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PolicyForm()
    return render(request, 'createPolicy.html', {'form': form})