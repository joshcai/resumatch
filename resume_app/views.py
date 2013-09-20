# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
import datetime

# from resume_app.models import Users
def index(request):
	return render(request, 'resume_app/index.html')