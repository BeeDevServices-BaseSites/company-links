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
    dept = models.ForeignKey(Department, related_name='theDepartment', on_delete=CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.dept.department}'
    
    def policyDept(self):
        return self.dept.department
    
    def policyAuthor(self):
        return self.author.first_name