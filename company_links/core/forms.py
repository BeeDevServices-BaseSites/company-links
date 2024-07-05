from django import forms
from .models import *

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['title', 'content', 'cat', 'author', 'dept']