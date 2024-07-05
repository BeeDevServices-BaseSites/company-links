from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import *
import bcrypt

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    authUser = AuthUser.objects.filter(email = request.POST['email'])
    # if added to authuser by management
    print('user', user, 'authUser', authUser)
    if authUser:
        # check if they have registered an account
        # if they have been added check if active account
        theAuthUser = authUser[0]
        if theAuthUser.active == True:
            if user:
                userLogin = user[0]
                # check password
                if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
                    request.session['user_id'] = userLogin.id
                    return redirect('/')
                messages.error(request, 'Invalid Credentials')
                return redirect('/')
            # if not registered
            messages.error(request, 'Username not in our system, please create an account using the email you provided Management')
            return redirect('/')
        # If not an active user
        messages.error(request, 'User Inactive! Please see Management!!')
    # If not part of authuser
    messages.error(request, 'Please see Management regarding an account')
    return redirect('/')

def reg(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/')
    hashedPW = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        username = request.POST['username'],
        email = request.POST['email'],
        password = hashedPW
    )
    request.session['user_id'] = newUser.id
    if newUser.id == 1:
        toUpdate = User.objects.get(id=request.session['user_id'])
        toUpdate.level=24
        toUpdate.role = 'Webmaster'
        toUpdate.save()
    messages.error(request, f'Welcome {newUser.first_name}')
    request.session['role'] = newUser.role
    return redirect('/')