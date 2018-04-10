# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.



class Profile(models.Model):
	#user_id=models.IntegerField()
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	birth_date=models.DateField(null=True,blank=True)

	def get_absolute_url(self):
		return reverse('Entry:index')

	def __str__(self):
		return self.user.username

class Genre(models.Model):
	#genre_id=models.IntegerField()
	genre_name=models.CharField(max_length=20)

	def __str__(self):
		return self.genre_name

class Writing_Style(models.Model):
	writing_style=models.CharField(max_length=20)

	def __str__(self):
		return self.writing_style



class Entry(models.Model):
	#entry_id=models.IntegerField()
	entry_name=models.CharField(max_length=40)
	entry_description=models.CharField(max_length=5000,default='Empty')
	entry_style=models.ForeignKey(Writing_Style,on_delete=models.CASCADE)
	entry_genres=models.ManyToManyField(Genre)
	entry_writer_id=models.ForeignKey(User,on_delete=models.CASCADE)
	entry_release_date=models.DateTimeField(default=timezone.now,blank=True)

	def get_absolute_url(self):
		return reverse('Entry:detail',kwargs={'pk':self.pk})
	def __str__(self):
		return self.entry_name



class Interest(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	genre=models.ForeignKey(Genre,on_delete=models.CASCADE)

class Follow(models.Model):
	following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
	follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')

	

class Saves(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	entry=models.ForeignKey(Entry,on_delete=models.CASCADE)

class Likes(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	entry=models.ForeignKey(Entry,on_delete=models.CASCADE)

# class Reviewer(models.Model):
# 	reviewer=models.ForeignKey(User,on_delete=models.CASCADE)
# 	entries=models.ManyToManyField(Entry,through='Ratings')


# class Ratings(models.Model):
# 	reviewer=models.ForeignKey(Reviewer,on_delete=models.CASCADE)
# 	entry=models.ForeignKey(Entry,on_delete=models.CASCADE)
# 	stars=models.IntegerField( validators=[MaxValueValidator(5)])


