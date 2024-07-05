from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import *

# title = {
#     'title': '',
#     'header': '',
# }
# prev_url = request.session['url']
# request.session['prev_url'] = prev_url

def index(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in")
        return render(request, 'logReg.html')
    else:
        user = User.objects.get(id=request.session['user_id'])
        role = user.role
        request.session['role']= role
    return render(request, 'index.html')

def temp(request):
    return render(request, 'temp.html')