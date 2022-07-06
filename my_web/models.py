from enum import unique
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from pkg_resources import require
from category.models import Category
# Create your models here.
class My_website(models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="my_website", blank=True)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name