# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.files import File
import os
import StringCompare
import datetime

from resume_app.models import User, Job,  Edu, Exp, Tag, Skill, Skill_Set, Honor, Additional, Additional_Section, Info, Resume, Comment

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
		resumes = Resume.objects.all().exclude(private=1)
		context = {
				'request':request,
				'resumes':resumes,
		}
		return render(request, 'resume_app/explore.html', context)
	return render(request, 'resume_app/explore_static.html', {'request':request})

def build(request):
	request.session['home'] = ''
	request.session['explore'] = ''
	request.session['build'] = 'a'
	request.session['match'] = ''
	if request.session.get('logged_in',False):
		user = User.objects.get(username=request.session['logged_in'])
		educations = Edu.objects.all().filter(user_id = user)
		experiences = Exp.objects.all().filter(user_id = user)
		honors = Honor.objects.all().filter(user_id = user)
		sets = Skill_Set.objects.all().filter(user_id= user)
		tags = Tag.objects.all().filter(user_id=user)
		skills = Skill.objects.all()
		context={
				'request':request,
				'educations':educations,
				'experiences':experiences,
				'honors':honors,
				'sets':sets,
				'tags':tags,
				'skills':skills,
			}


		return render(request, 'resume_app/build.html', context)
	return render(request, 'resume_app/build_static.html', {'request':request})


def generated(request, file_name):
	return render(request, 'resume_app/generated.html', {'request':request, 'file_name':file_name})

def display(request, file_name):
	if request.method == 'POST' and request.POST['comment']:
		user = User.objects.get(username=request.session['logged_in'])
		resume = Resume.objects.filter(resume=file_name)[0]
		com = Comment(comment=request.POST['comment'],user_id=user,resume=resume)
		com.save()
		return HttpResponseRedirect(reverse('resume_app:display', kwargs={'file_name':file_name}))
	resume = Resume.objects.filter(resume=file_name)[0]
	comments = Comment.objects.filter(resume=resume).order_by('pk').reverse()
	return render(request, 'resume_app/display.html',{'request':request, 'resume':resume, 'comments':comments})

def addskill(request):
	if request.method == 'POST':
		skill_set = Skill_Set.objects.filter(pk=request.POST['skill_set'])[0]
		s = Skill(name=request.POST['name'], skill_set = skill_set)
		s.save()
	return HttpResponseRedirect(reverse('resume_app:build'))


def save_resume(request):
	if request.method == 'POST':
		user = User.objects.get(username=request.session['logged_in'])
		name = request.POST['file_name']
		skill_string=request.session['skill_string']
		skill_sets = Skill_Set.objects.filter(user_id=user)
		
		private = False
		if 'private' in request.POST:
			private = True
		res = Resume(user_id=user,
			resume=name,
			upvotes=0,
			private=private,
			skill_string=skill_string,
			)
		res.save()
		os.system('cp resume_app/generated/'+request.POST['old_file_name']+'.pdf resume_app/generated/' + request.POST['file_name']+'.pdf')
	return HttpResponseRedirect(reverse('resume_app:match'))

	# with open("/home/josh/Desktop/projects/resumemaker/resume_app/generated/template.tex") as template:
	# 	templ = File(template)
	# 	print templ.read()



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
		tags = Tag.objects.filter(user_id=user)
		for tag in tags:
			if tag.name in request.POST:
				e.tags.add(tag)
	return HttpResponseRedirect(reverse('resume_app:build'))
#Experience controller
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
		tags = Tag.objects.filter(user_id=user)
		for tag in tags:
			if tag.name in request.POST:
				e.tags.add(tag)
	return HttpResponseRedirect(reverse('resume_app:build'))

#Honors Controller
def honors(request):
	if request.method == 'POST':
		# d = datetime.datetime.now()
		user = User.objects.get(username=request.session['logged_in'])
		h = Honor(user_id=user,
			name = request.POST['name'],
			location = request.POST['location'],
			date = request.POST['date'],
			# tags = models.ManyToManyField(Tag)
			descriptions = request.POST['description'],
			# date=d,
			# date_str=d.strftime('%B %d, %Y')
		)
		h.save()
		tags = Tag.objects.filter(user_id=user)
		for tag in tags:
			if tag.name in request.POST:
				h.tags.add(tag)
	return HttpResponseRedirect(reverse('resume_app:build'))

def skillset(request):
	if request.method == 'POST':
		# d = datetime.datetime.now()
		user = User.objects.get(username=request.session['logged_in'])
		s = Skill_Set(user_id=user,
			name = request.POST['name'],
			# tags = models.ManyToManyField(Tag)
		)
		s.save()
		tags = Tag.objects.filter(user_id=user)
		for tag in tags:
			if tag.name in request.POST:
				s.tags.add(tag)
	return HttpResponseRedirect(reverse('resume_app:build'))

def addjob(request):
	if request.method == 'POST':
		j = Job(title=request.POST['title'], description = request.POST['description'], skills=request.POST['skills'])
		j.save()
	return HttpResponseRedirect(reverse('resume_app:match'))
def create_tag(request):
	if request.method == 'POST':
		user = User.objects.get(username=request.session['logged_in'])
		t = Tag(user_id=user, name=request.POST['tag_name'])
		t.save()
	return HttpResponseRedirect(reverse('resume_app:build'))
def match(request):
	request.session['home'] = ''
	request.session['explore'] = ''
	request.session['build'] = ''
	request.session['match'] = 'a'
	if request.session.get('logged_in',False):
		jobs = Job.objects.all()
		user = User.objects.get(username=request.session['logged_in'])
		resumes = Resume.objects.filter(user_id=user)
		add_permission = (user.username == 'job')
		context={
				'request':request,
				'jobs': jobs,
				'add_permission':add_permission,
				'resumes':resumes,
		}
		return render(request, 'resume_app/match.html', context)
	return render(request, 'resume_app/match_static.html', {'request':request})

def matched(request, file_name):
	resume = Resume.objects.filter(resume=file_name)[0]
	jobs = Job.objects.all()
	user = User.objects.get(username=request.session['logged_in'])
	resumes = Resume.objects.filter(user_id=user)
	max_ratio=0
	max_ref = jobs[0]
	for job in jobs:
		ratio = StringCompare.matchWords(job.skills.encode('utf-8'), resume.skill_string.encode('utf-8'))
		print ratio
		if ratio > max_ratio:
			max_ref = job
			max_ratio = ratio
	context={
			'request':request,
			'matched': True,
			'job': max_ref,
			'resume': resume,
	}
	return render(request, 'resume_app/match.html',context)

def generate(request):
	user = User.objects.get(username=request.session['logged_in'])
	query = Q()
	tags = Tag.objects.filter(user_id=user)
	if request.method == 'POST':
		for tag in tags:
			if tag.name in request.POST:
				print 'hello'
				query = query | Q(tags__name=tag.name)
				print query
	query = query & Q(user_id=user)
	education = Edu.objects.filter(query).distinct()
	print education
	experience = Exp.objects.filter(query).distinct()
	honors = Honor.objects.filter(query).distinct()
	skill_set = Skill_Set.objects.filter(query).distinct()
	template = r"""
\documentclass[line,margin]{res}
%\usepackage{helvetica} % uses helvetica postscript font (download helvetica.sty)
%\usepackage{newcent}   % uses new century schoolbook postscript font 

\begin{document}"""
	user = User.objects.get(username=request.session['logged_in'])
	template+=r"\name{%s}" % user.name
	template+=r"""
	\begin{resume}
"""
 
 	if education:
 		template+=r'\section{EDUCATION}'
 		for edu in education:
			template+=r"{\sl "+edu.degree+r"}, GPA: " +edu.gpa +r" \\"
			template+=edu.university+', '+edu.start+"-"+edu.finish
			if edu.descriptions != '':
				template+=r'\begin{itemize} \itemsep -2pt'
				descripts = edu.descriptions.splitlines()
				for descript in descripts:
					template+=r'\item '+descript
				template+=r'\end{itemize} '		
	if experience:
		template+=r'\section{EXPERIENCE}'
		for exp in experience:
			template+=r"{\sl "+exp.position+r"} \hfill " + exp.start + " - " + exp.finish+r'\\'
			template+=exp.company+", "+exp.location
			if exp.descriptions != '':
				template+=r'\begin{itemize} \itemsep -2pt'
				descripts = exp.descriptions.splitlines()
				for descript in descripts:
					template+=r'\item '+descript
				template+=r'\end{itemize} '		
	if skill_set:
		template+=r'\section{KNOWLEDGE AND SKILLS}'
		for skill_s in skill_set:
			template+=r"{\sl "+skill_s.name+r":} "
			skills = Skill.objects.filter(skill_set=skill_s)
			for skill in skills:
				template+=skill.name+", "
			template+=r"\\"
	if honors:
		template+=r'\section{HONORS}'
		for honor in honors:
			template+=r"{\sl "+honor.name+r",} " + honor.location + r" \hfill " + honor.date +r'\\'
			if honor.descriptions != '':
				template+=r'\begin{itemize} \itemsep -2pt'
				descripts = honor.descriptions.splitlines()
				for descript in descripts:
					template+=r'\item '+descript
				template+=r'\end{itemize} '	

 

	template+="""\end{resume}
\end{document}"""
	file_name = ''.join(user.name.split())
	f = open(file_name + '.tex', 'w')
	f.write(template)
	f.close()
	print file_name
	os.system('pdflatex ' + file_name + '.tex')
	os.system('mv ' + file_name + '.pdf resume_app/generated/')
	os.system('rm ' + file_name + '.log')
	os.system('rm ' + file_name + '.tex')
	skill_string=''
	for sets in skill_set:
			skill_string+=sets.name+' '
			skills = Skill.objects.filter(skill_set=sets)
			for skill in skills:
				skill_string+=skill.name+' '
	request.session['skill_string'] = skill_string
	return HttpResponseRedirect(reverse('resume_app:generated', kwargs={'file_name':file_name}))
