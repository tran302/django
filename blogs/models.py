import os
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # only if you need to support Python 2
class Blog(models.Model):
    # blog model
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    domain = models.URLField(max_length=200, unique=True)
    is_public = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
	
    def __str__(self):
        return self.title


@python_2_unicode_compatible  # only if you need to support Python 2
class Category(models.Model):
	# category model
    class Meta:
        # to fix naming categorys to categories
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100, unique=True)
	
    def __str__(self):
        return self.name
		
@python_2_unicode_compatible  # only if you need to support Python 2
class Tag(models.Model):
    # tag model
    name = models.CharField(max_length=100, unique=True)
	
    def __str__(self):
        return self.name


@python_2_unicode_compatible  # only if you need to support Python 2
class Post(models.Model):
    # post model
    title = models.CharField(max_length=100)
    body = models.TextField()
    video = models.URLField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    blog = models.ForeignKey(Blog)
	
    def __str__(self):
        return self.title
		
		
@python_2_unicode_compatible  # only if you need to support Python 2
class Image(models.Model):
    # image model
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    post = models.ForeignKey(Post)
	
    def __str__(self):
        return self.name
		
