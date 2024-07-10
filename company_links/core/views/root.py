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
        policies = Policy.objects.filter(dept__level__lte=user.level)
        departments = Department.objects.filter(level__lte=user.level)
        categories = Category.objects.values().all()
        links = Link.objects.filter(theDept__level__lte=user.level)
        docs = Doc.objects.filter(docDept__level__lte=user.level)
        context = {
            'user': user,
            'role': role,
            'policies': policies,
            'departments': departments,
            'categories': categories,
            'links': links,
            'docs': docs,
        }
        print('user', user, 'policies', policies, 'docs', docs, 'links', links)
        return render(request, 'index.html', context)

def logout(request):
    request.session.clear()
    messages.error(request, 'You have ben logged out')
    return redirect('/')

def viewPolicy(request, policy_id):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        role = request.session['role']
        policy = get_object_or_404(Policy, id=policy_id)
        context = {
            'policy': policy,
            'user': user,
            'role': role,
        }
        return render(request, 'viewPolicy.html', context)

def viewDoc(request, doc_id):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        role = request.session['role']
        doc = get_object_or_404(Doc, id=doc_id)
        context = {
            'doc': doc,
            'user': user,
            'role': role,
        }
        return render(request, 'viewDoc.html', context)

def createPolicy(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
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
    
def editPolicy(request, policy_id):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        role = request.session['role']
        policy = get_object_or_404(Policy, id=policy_id)
        if request.method == 'POST':
            form = PolicyForm(request.POST, instance=policy)
            if form.is_valid:
                form.save()
                return redirect('/viewPolicy/')
        else:
            form = PolicyForm(instance=policy)
        context = {
                'user': user,
                'role': role,
                'policy': policy,
                'form': form,
        }
        return render(request, 'editPolicy.html', context)
