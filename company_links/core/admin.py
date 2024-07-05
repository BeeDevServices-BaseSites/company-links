from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms

admin.site.register(Department)
admin.site.register(Category)
# admin.site.register(Policy)

class PolicyAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Policy
        fields = '__all__'

class PolicyAdmin(admin.ModelAdmin):
    form = PolicyAdminForm

admin.site.register(Policy, PolicyAdmin)