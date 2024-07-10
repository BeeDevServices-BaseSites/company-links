from django.db import models
from django.db.models.deletion import CASCADE
from user.models import *
from ckeditor.fields import RichTextField

class Department(models.Model):
    department = models.CharField(max_length=255)
    level = models.IntegerField()

    def __str__(self):
        return f'{self.department} - Level {self.level}'
    
class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
    
class Policy(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    cat = models.ForeignKey(Category, related_name='theCategory', on_delete=CASCADE, blank=True)
    author = models.ForeignKey(AuthUser, related_name='theAuthor', on_delete=CASCADE)
    dept = models.ForeignKey(Department, related_name='theDepartment', on_delete=CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.dept.department if self.dept else "No Department"}'

    def policyDept(self):
        return self.dept.department if self.dept else "No Department"
    
    def policyAuthor(self):
        return self.author.first_name

class Doc(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    docCat = models.ForeignKey(Category, related_name='docCategory', on_delete=CASCADE, blank=True)
    docAuthor = models.ForeignKey(AuthUser, related_name='docAuthor', on_delete=CASCADE)
    docDept = models.ForeignKey(Department, related_name='docDepartment', on_delete=CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.docDept.department if self.docDept else "No Department"}'

    def policyDept(self):
        return self.docDept.department if self.docDept else "No Department"
    
    def policyAuthor(self):
        return self.docAuthor.first_name

class Link(models.Model):
    name = models.CharField(max_length=255)
    url = models.TextField()
    theCat = models.ForeignKey(Category, related_name='theCat', on_delete=CASCADE, blank=True)
    creator = models.ForeignKey(AuthUser, related_name='theCreator', on_delete=CASCADE)
    theDept = models.ForeignKey(Department, related_name='theDept', on_delete=CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.theDept.department if self.theDept else "No Department"}'
    
    def linkDept(self):
        return self.theDept.department if self.theDept else "No Department"
    
    def linkAuthor(self):
        return self.creator.first_name