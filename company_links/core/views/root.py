from django.shortcuts import render, redirect
from django.contrib import messages


# title = {
#     'title': '',
#     'header': '',
# }
# prev_url = request.session['url']
# request.session['prev_url'] = prev_url

def index(request):
    return render(request, 'index.html')

def temp(request):
    return render(request, 'temp.html')