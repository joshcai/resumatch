from django.db import models

# Create your models here.


class User(models.Model):
	username = models.CharField(max_length=120)
	password = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	name = models.CharField(max_length=120)
	def __unicode__(self):
		return self.username


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
