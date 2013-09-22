from django.conf.urls import patterns, url

from resume_app import views

from django.conf import settings


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^explore/$', views.explore, name='explore'),
	url(r'^build/$', views.build, name='build'),
	url(r'^update_education/$', views.education, name='update_education'),
	url(r'^update_experience/$', views.experience, name='update_experience'),
	url(r'^update_honors/$', views.honors, name='update_honors'),
	url(r'^update_skill_set/$', views.skillset, name='update_skill_set'),
	url(r'^match/$', views.match, name='match'),
	url(r'^generate/$', views.generate, name='generate'),
	url(r'^add_skill/$', views.addskill, name='add_skill'),
	url(r'^add_job/$', views.addjob, name='add_job'),
	url(r'^generated/(?P<file_name>.*)/$', views.generated, name='generated'),
	url(r'^display/(?P<file_name>.*)/$', views.display, name='display'),
	url(r'^matched/(?P<file_name>.*)/$', views.matched, name='matched'),
	url(r'^save_resume/$', views.save_resume, name='save_resume'),
	url(r'^create_tag/$', views.create_tag, name='create_tag'),

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

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT}))