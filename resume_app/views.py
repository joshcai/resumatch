# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.files import File
import datetime

from resume_app.models import User, Edu, Exp, Tag, Skill, Skill_Set, Honor, Additional, Additional_Section, Info

# from resume_app.models import Users
def index(request):
	request.session['home'] = 'a'
	request.session['explore'] = ''
	request.session['build'] = ''
	request.session['match'] = ''
	return render(request, 'resume_app/index.html', {'request':request})

def signup(request):
	if request.method == 'POST':
		if request.POST['name'] and request.POST['username'] and request.POST['email'] and request.POST['password'] and request.POST['password_confirm'] and request.POST['password'] == request.POST['password_confirm']:
			# d = datetime.datetime.now()
			u = User(username=request.POST['username'],
				password=request.POST['password'],
				email=request.POST['email'],
				name=request.POST['name'],
				# date=d,
				# date_str=d.strftime('%B %d, %Y')
			)
			u.save()
			return HttpResponseRedirect(reverse('resume_app:index'))
		else:
			context={
				'username': request.POST['username'],
				'name': request.POST['name'],
				'email': request.POST['email'],
				'error_message': "Please fill in all fields or password mismatch <br />",
				'request':request,
			}
			return render(request, 'resume_app/signup.html', context)
	return render(request, 'resume_app/signup.html', {'request': request})

def login(request):
	if request.method == 'POST':
		if request.POST['username']:
			userexists = True
			try:
				user = User.objects.get(username=request.POST['username'])
			except ObjectDoesNotExist:
				userexists = False
		if request.POST['username'] and userexists and request.POST['password'] and request.POST['password'] == user.password:
			request.session['logged_in'] = user.username
			return render(request, 'resume_app/index.html', {'request':request})
		else:
			context={
				'username': request.POST['username'],
				'error_message': "Username or password incorrect <br/>",
				'request': request,
			}
			return HttpResponseRedirect(reverse('resume_app:index'))
	return render(request, 'resume_app/login.html', {'request':request})

def logout(request):
	try:
		del request.session['logged_in']
	except KeyError:
		pass
	return HttpResponseRedirect(reverse('resume_app:index'))


def explore(request):
	request.session['home'] = ''
	request.session['explore'] = 'a'
	request.session['build'] = ''
	request.session['match'] = ''
	if request.session.get('logged_in',False):
		return render(request, 'resume_app/index.html', {'request':request})
	return render(request, 'resume_app/explore_static.html', {'request':request})

def build(request):
	request.session['home'] = ''
	request.session['explore'] = ''
	request.session['build'] = 'a'
	request.session['match'] = ''
	if request.session.get('logged_in',False):
		user = User.objects.get(username=request.session['logged_in'])
		educations = Edu.objects.all().filter(user_id = user)
		context={
				'request':request,
				'educations':educations,
			}
		return render(request, 'resume_app/build.html', context)
	return render(request, 'resume_app/build_static.html', {'request':request})

def education(request):
	if request.method == 'POST':
		# d = datetime.datetime.now()
		user = User.objects.get(username=request.session['logged_in'])
		e = Edu(user_id=user,
			university = request.POST['university'],
			gpa =request.POST['gpa'],
			degree = request.POST['degree'],
			start = request.POST['start'],
			finish = request.POST['finish'],
			# tags = models.ManyToManyField(Tag)
			descriptions = request.POST['description'],
			# date=d,
			# date_str=d.strftime('%B %d, %Y')
		)
		e.save()
	return HttpResponseRedirect(reverse('resume_app:build'))
//Experience controller
def experience(request):
	if request.method == 'POST':
		# d = datetime.datetime.now()
		user = User.objects.get(username=request.session['logged_in'])
		e = Exp(user_id=user,
			company = request.POST['company'],
			position =request.POST['position'],
			location = request.POST['location'],
			start = request.POST['start'],
			finish = request.POST['finish'],
			# tags = models.ManyToManyField(Tag)
			descriptions = request.POST['description'],
			# date=d,
			# date_str=d.strftime('%B %d, %Y')
		)
		e.save()
	return HttpResponseRedirect(reverse('resume_app:build'))

//Honors Controller
def honors(request):
	if request.method == 'POST':
		# d = datetime.datetime.now()
		user = User.objects.get(username=request.session['logged_in'])
		e = Honors(user_id=user,
			name = request.POST['name'],
			position =request.POST['position'],
			location = request.POST['location'],
			date = request.POST['date'],
			# tags = models.ManyToManyField(Tag)
			descriptions = request.POST['description'],
			# date=d,
			# date_str=d.strftime('%B %d, %Y')
		)
		e.save()
	return HttpResponseRedirect(reverse('resume_app:build'))

def match(request):
	request.session['home'] = ''
	request.session['explore'] = ''
	request.session['build'] = ''
	request.session['match'] = 'a'
	if request.session.get('logged_in',False):
		return render(request, 'resume_app/index.html', {'request':request})
	return render(request, 'resume_app/match_static.html', {'request':request})
# 	def render_post(content):
# 	array_str = content.splitlines()
# 	new_content = ""
# 	for temp in array_str:
# 		if temp=="":
# 			new_content+="<br />\n"
# 		else:
# 			new_content+="<p>"+temp+"</p>\n"
# 	return new_content

# def index(request, page_num=1):
# 	tags = Tag.objects.all()
# 	query = Q()
# 	if 'filter' in request.GET:
# 		filtered = True
# 		flag = True
# 		for tag in tags:
# 			if tag.descript not in request.GET:
# 				request.session[tag.descript] = False
# 			else:
# 				request.session[tag.descript] = True
# 				flag = False
# 				query = query | Q(tags__descript=tag.descript)
# 		if flag:
# 			query = Q(deleted=True) & Q(deleted=False) # returns none - better way to do this?
# 	else:
# 		filtered = False
# 		for tag in tags:
# 			if tag.descript not in request.session: # this line preserves filters through sessions regardless of filter status
# 				request.session[tag.descript] = True
# 			elif request.session[tag.descript]:
# 				query = query | Q(tags__descript=tag.descript)
# 	blog_entries = Post.objects.order_by('-date').distinct().filter(query).exclude(deleted=True)
# 	context ={
# 		'blog_entries': blog_entries[(float(page_num)-1)*5:float(page_num)*5],
# 		'page_num': page_num,
# 		'request': request,
# 		'tags': tags,
# 		}
# 	if filtered:
# 		context['filtered'] = True
# 	if float(page_num) > 1:
# 		context['prev'] = True
# 	if float(page_num)*5 < len(blog_entries): # this can be optimized later - (code is already hitting database once)
# 		context['next'] = True

# 	return render(request, 'blog/index.html', context)

# def newpost(request):
# 	if 'logged_in' in request.session and request.session['logged_in']:
# 		tags = Tag.objects.all()
# 		if request.method == 'POST':
# 			if request.POST['subject'] and request.POST['content']:
# 				d = datetime.datetime.now()
# 				p = Post(subject=request.POST['subject'], content=request.POST['content'], content_rendered=render_post(request.POST['content']), date=d, date_str=d.strftime('%B %d, %Y'))
# 				p.save()
# 				for tag in tags:
# 					if tag.descript in request.POST:
# 						p.tags.add(tag)
# 				return HttpResponseRedirect(reverse('blog:index'))
# 			else:
# 				context={
# 					'subject': request.POST['subject'],
# 					'content': request.POST['content'],
# 					'error_message': "Please fill in all fields<br />",
# 					'url': reverse('blog:newpost'),
# 					'title': "New Post",
# 					'request': request,
# 					'tags': tags,
# 				}
# 				return render(request, 'blog/newpost.html', context)
# 		return render(request, 'blog/newpost.html', {'url': reverse('blog:newpost'), 'title': "New Post", 'request': request, 'tags': tags})
# 	else:
# 		return HttpResponseRedirect(reverse('blog:index'))

# def update(request, post_id):
# 	if 'logged_in' in request.session and request.session['logged_in']:
# 		post = get_object_or_404(Post, pk=post_id)
# 		tags = Tag.objects.all()
# 		context={
# 			'post': post,
# 			'url': reverse('blog:update', kwargs={'post_id': post_id}),
# 			'title': "Update",
# 			'request': request,
# 			'tags': tags,
# 		}
# 		if request.method == 'POST':
# 			if request.POST['subject'] and request.POST['content']:
# 				post.subject = request.POST['subject']
# 				post.content = request.POST['content']
# 				post.content_rendered = render_post(request.POST['content'])
# 				post.save()
# 				for tag in tags:
# 					if tag.descript in request.POST:
# 						post.tags.add(tag)
# 					else:
# 						post.tags.remove(tag)
# 				return HttpResponseRedirect(reverse('blog:index'))
# 			else:
# 				context['subject'] = request.POST['subject']
# 				context['content'] = request.POST['content']
# 				context['error_message'] = "Please fill in all fields<br />"
# 		return render(request, 'blog/newpost.html', context)
# 	else:
# 		return HttpResponseRedirect(reverse('blog:index'))

# def login(request):
# 	context={'request': request}
# 	if request.method == 'POST':
# 		if request.POST['password'] == secrets.login_password:
# 			request.session['logged_in'] = True
# 			return HttpResponseRedirect(reverse('blog:index'))
# 		else:
# 			context['error_message'] = "Invalid password<br />"
# 	return render(request, 'blog/login.html', context)

# def logout(request):
# 	request.session['logged_in'] = False
# 	return HttpResponseRedirect(reverse('blog:index'))

# def delete(request, post_id):
# 	if 'logged_in' in request.session and request.session['logged_in']:
# 		post = get_object_or_404(Post, pk=post_id)
# 		post.deleted = True
# 		post.save()
# 		return HttpResponseRedirect(reverse('blog:index'))

# def post(request, post_id):
# 	post = get_object_or_404(Post, pk=post_id)
# 	context={
# 		'post': post,
# 		'request': request,
# 	}
# 	tags = Tag.objects.all()
# 	query = Q()
# 	for tag in tags:
# 		if request.session[tag.descript]:
# 			query = query | Q(tags__descript=tag.descript)
# 	query = Post.objects.filter(query).exclude(deleted=True)
# 	next = query.filter(pk__gt=post_id)
# 	if next:
# 		context['next'] = next[0]
# 	prev = query.filter(pk__lt=post_id).order_by('id').reverse()
# 	if prev:
# 		context['prev'] = prev[0]
# 	return render(request,'blog/post.html', context)
