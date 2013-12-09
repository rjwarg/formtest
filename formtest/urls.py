from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'form1.views.index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^form1/', include('form1.urls')),
  #  url(r'^accounts/login/$', include('form1.urls')),
    url(r'^$', 'form1.views.index', name="index"),
    url(r'^index/$', 'form1.views.index'),
    url(r'^login/$', 'form1.views.login_user'),
    url(r'^stub/$', 'form1.views.stub', name='stub'),
    url(r'^accounts/login/$', 'form1.views.login_user'),
    url(r'^seek_person/$', 'form1.views.seekperson'),
    url(r'^logout/$', 'form1.views.my_logout', name="logout"),
)
