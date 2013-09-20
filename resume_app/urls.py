from django.conf.urls import patterns, url

from resume_app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	# url(r'^login/$', views.login, name='login'),
	# url(r'^blog/login/$', views.login, name='login_redirect'),
	# url(r'^logout/$', views.logout, name='logout'),
	# url(r'^blog/$', views.index, name='index'),
	# url(r'^blog/(?P<page_num>\d+)/$', views.index, name='index_num'),
	# url(r'^blog/newpost/$', views.newpost, name='newpost'),
	# url(r'^blog/update/(?P<post_id>\d+)/$', views.update, name='update'),
	# url(r'^blog/delete/(?P<post_id>\d+)/$', views.delete, name='delete'),
	# url(r'^blog/post/(?P<post_id>\d+)/$', views.post, name='post'),
	)