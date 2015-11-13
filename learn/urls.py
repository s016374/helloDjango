from learn import views

__author__ = 's016374'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.current_datetime),
)
