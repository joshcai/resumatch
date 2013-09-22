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

def generate(request):
	template = r"""
\documentclass[line,margin]{res}
%\usepackage{helvetica} % uses helvetica postscript font (download helvetica.sty)
%\usepackage{newcent}   % uses new century schoolbook postscript font 

\begin{document}"""
	user = User.objects.get(username=request.session['logged_in'])
	template+=r"\name{%s}" % user.name
	template+=r"""
	\begin{resume}
 
\section{OBJECTIVE}       A position in the field of computers with special 
                interests in business applications programming, 
                information processing, and management systems. 
 
 
\section{EDUCATION} {\sl Bachelor of Science,} Interdisciplinary Science \\
                % \sl will be bold italic in New Century Schoolbook (or
	        % any postscript font) and just slanted in
		% Computer Modern (default) font
                Rensselaer Polytechnic Institute, Troy, NY, 
                expected December 1990 \\
                Concentration: Computer Science \\
                Minor: Management 
 
 
\section{COMPUTER \\ SKILLS} {\sl Languages \& Software:} COBOL, IFPS, Focus, 
         Megacalc, Pascal, Modula2, C, APL, SNOBOL, 
                FORTRAN, LISP, SPIRES, BASIC, VSPC Autotab, 
                IBM 370 Assembler, Lotus 1-2-3. \\
                {\sl Operating Systems:} MTS, TSO, Unix.
 
\section{EXPERIENCE} {\sl Business Applications Programmer} \hfill Fall 1990 \\
                Allied-Signal Bendix Friction Materials Division, 
                Financial Planning Department, Latham, NY
                 \begin{itemize}  \itemsep -2pt % reduce space between items
                 \item Developed four "user friendly" forecasting 
                    systems each of which produces 18 to 139 
                    individual reports. 
                \item   Developed or improved almost all IFPS 
                    programs used for financial reports. 
                \end{itemize}
 
                {\sl Research Programmer} \hfill            Summer 1990 \\
                Psychology Department, Rensselaer Polytechnic 
                Institute 
                 \begin{itemize}  \itemsep -2pt %reduce space between items
                 \item Performed computer aided statistical analysis 
                    of data. 
                 \end{itemize} 
                {\sl Assistant Manager} \hfill        Summers 1988-89 \\
                Thunder Restaurant, Canton, CT
                  \begin{itemize}
                   \item Recognized need for, developed, and wrote 
                    employee training manual. Performed various 
                    duties including cooking, employee training, 
                    ordering, and inventory control. 
                   \end{itemize} 
 
\section{COMMUNITY \\ SERVICE}  Organized and directed the 1988 and 1989 Grand 
                 Marshall Week \newline ``Basketball Marathon.'' A 24 hour 
                charity event to benefit the Troy Boys Club. Over 
                250 people participated each year. 

\section{EXTRA-CURRICULAR \\ ACTIVITIES}             
            Elected {\it House Manager}, Rho Phi Sorority \\
            Elected {\it Sports Chairman} \\
            Attended Krannet Leadership Conference \\
                Headed delegation to Rho Phi Congress \\
                Junior varsity basketball team \\
                Participant, seven intramural athletic teams 
 

\end{resume}
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
	return HttpResponseRedirect(reverse('resume_app:generated', kwargs={'file_name':file_name}))

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
		skill_string=''
		skill_sets = Skill_Set.objects.filter(user_id=user)
		for sets in skill_sets:
			skill_string+=sets.name+' '
			skills = Skill.objects.filter(skill_set=sets)
			for skill in skills:
				skill_string+=skill.name+' '
		print skill_string
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
	return HttpResponseRedirect(reverse('resume_app:generated', kwargs={'file_name':name}))

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
	}
	return render(request, 'resume_app/match.html',context)


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
