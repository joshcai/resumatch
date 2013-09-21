from django.db import models

# Create your models here.


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


class Skill(models.Model):
	name = models.CharField(max_length=120)
	def __unicode__(self):
		return self.name

class Skill_Set(models.Model):
	user_id = models.ForeignKey(User)
	name = models.CharField(max_length=120)
	skills = models.ManyToManyField(Skill)
	tags = models.ManyToManyField(Tag)
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
	user_id = models.IntegerField()


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
