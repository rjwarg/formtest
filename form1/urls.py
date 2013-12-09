from django.conf.urls import patterns, include, url

from form1 import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'formtest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^$', views.index, name="index"),
   url(r'^addperson/$', views.addperson, name="addperson"),
   url(r'^seekperson/$', views.seekperson, name="seekperson"),
 #   url(r'^showmember/(.+)/$', views.showmember, name="showmember"),
   url(r'^stub/$', views.stub, name='stub'),
   url(r'^accounts/login/$', views.stub),
   url(r'^logout/$', views.my_logout, name="logout"),
   
    )

