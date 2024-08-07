from django.db import models
from django.core.validators import RegexValidator
import re

class AuthUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    active_date = models.DateTimeField(auto_now=True)
    deactivate_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.active:
            return f'{self.first_name} - Active'
        else:
            return f'{self.first_name} - Inactive'

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        auth_email = AuthUser.objects.filter(email=form['email'], active=True)
        email_check = self.filter(email=form['email'])
        username_check = self.filter(username=form['username'])
        if not auth_email:
            errors['email']= 'Unauthorized / Inactive email. Please see Management'
        if email_check:
            errors['email'] = 'Email already in use'
        if username_check:
            errors['username'] = 'Username already in use'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255, default='General')
    level = models.IntegerField(default=1)

    objects = UserManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.username} - {self.first_name}'