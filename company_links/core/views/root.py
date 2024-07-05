from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.forms import *
from user.models import *
from core.models import *


def index(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in")
        user = False
        context = {
            'user': user
        }
        print('user', user)
        return render(request, 'logReg.html', context)
    else:
        user = User.objects.get(id=request.session['user_id'])
        request.session['role']= user.role
        role = request.session['role']
        policies = Policy.objects.values().all()
        departments = Department.objects.values().all()
        categories = Category.objects.values().all()
        print('policies', policies)
        context = {
            'user': user,
            'role': role,
            'policies': policies,
            'departments': departments,
            'categories': categories,
        }
        print('user', user)
        return render(request, 'index.html', context)

def logout(request):
    request.session.clear()
    messages.error(request, 'You have ben logged out')
    return redirect('/')

def viewPolicy(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    context = {
        'policy': policy,
    }
    return render(request, 'viewPolicy.html', context)

def createPolicy(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in")
        return render(request, 'logReg.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        request.session['role']= user.role
        role = request.session['role']
        if request.method == 'POST':
            form = PolicyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = PolicyForm()
        context = {
            'user': user,
            'role': role,
            'form': form,
        }
        return render(request, 'createPolicy.html', context)