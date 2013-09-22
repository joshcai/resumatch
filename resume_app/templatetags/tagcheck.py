from django import template

register = template.Library()

def tagcheck(value, arg):
	"""Gets the value of the tag in request session"""

	return str(value.id)==str(arg)

register.filter('tagcheck', tagcheck)

def tag(value, arg):
	if arg in value.tags.all():
		return True
	return False

register.filter('tag', tag)