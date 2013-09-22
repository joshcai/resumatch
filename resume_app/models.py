from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage()

class User(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	name = models.CharField(max_length=120)
	def __unicode__(self):
		return self.username


class Tag(models.Model):
	name = models.CharField(max_length=120)
	user_id = models.ForeignKey(User)
	def __unicode__(self):
		return self.name

class Edu(models.Model):
	user_id = models.ForeignKey(User)
	university = models.CharField(max_length=120)
	gpa = models.CharField(max_length=120)
	degree = models.CharField(max_length=120)
	start = models.CharField(max_length=120)
	finish = models.CharField(max_length=120)
	tags = models.ManyToManyField(Tag)
	descriptions = models.TextField(default="")
	def __unicode__(self):
		return self.university

class Exp(models.Model):
	user_id = models.ForeignKey(User)
	position = models.CharField(max_length=120)
	company = models.CharField(max_length=120)
	location = models.CharField(max_length=120)
	start = models.CharField(max_length=120)
	finish = models.CharField(max_length=120)
	tags = models.ManyToManyField(Tag)
	descriptions = models.TextField(default="")
	def __unicode__(self):
		return self.company


class Skill_Set(models.Model):
	user_id = models.ForeignKey(User)
	name = models.CharField(max_length=120)
	tags = models.ManyToManyField(Tag)
	def __unicode__(self):
		return str(self.id)


class Skill(models.Model):
	skill_set = models.ForeignKey(Skill_Set)
	name = models.CharField(max_length=120)
	def __unicode__(self):
		return self.name


class Honor(models.Model):
	user_id = models.ForeignKey(User)
	name = models.CharField(max_length=120)
	location = models.CharField(max_length=120)
	date = models.CharField(max_length=120)
	tags = models.ManyToManyField(Tag)
	descriptions = models.TextField(default="")
	def __unicode__(self):
		return self.university



class Additional(models.Model):
	user_id = models.ForeignKey(User)
	name = models.CharField(max_length=120)
	descriptions = models.TextField(default="")
	def __unicode__(self):
		return self.name


class Additional_Section(models.Model):
	user_id = models.ForeignKey(User)
	name = models.CharField(max_length=120)
	sections = models.ManyToManyField(Additional)
	def __unicode__(self):
		return self.name

class Info(models.Model):
	user_id = models.ForeignKey(User)


class Resume(models.Model):
	user_id = models.ForeignKey(User)
	resume = models.CharField(max_length=120)
	upvotes = models.IntegerField()
	skill_string = models.TextField(default="")
	private = models.BooleanField()



class Comment(models.Model):
	resume = models.ForeignKey(Resume)
	user_id = models.ForeignKey(User)
	comment = models.CharField(max_length=200)

class Job(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(default="")
	skills = models.TextField(default="")

# class Post(models.Model):
# 	subject = models.CharField(max_length=120)
# 	content = models.TextField()
# 	content_rendered = models.TextField(default="")
# 	date = models.DateTimeField('date created')
# 	date_str = models.CharField(max_length=120)
# 	deleted = models.BooleanField(default=False)
# 	tags = models.ManyToManyField(Tag)
# 	def __unicode__(self):
# 		return self.subject
