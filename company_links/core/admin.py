from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms

admin.site.register(Department)
admin.site.register(Category)
# admin.site.register(Policy)
admin.site.register(Link)

class PolicyAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Policy
        fields = '__all__'

class PolicyAdmin(admin.ModelAdmin):
    form = PolicyAdminForm

admin.site.register(Policy, PolicyAdmin)

class DocAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Doc
        fields = '__all__'

class DocAdmin(admin.ModelAdmin):
    form = DocAdminForm

admin.site.register(Doc, DocAdmin)