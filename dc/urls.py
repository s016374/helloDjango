import os
from django.conf.urls import patterns, include, url
from django.contrib import admin
from dc.views import current_datetime, hours_ahead, page1, hello, current_datetime_by_temp, hours_ahead_by_temp, hours_ahead_by_temp_by_render_to_response, \
    sample, carol
import learn


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
    # url(r'^learn/', 'learn.urls'),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^page1/$', page1),
    url(r'^timebytemp/$', current_datetime_by_temp),
    url(r'^timebytemp/plus/(\d{1,2})/add/(\d{1,2})$', hours_ahead_by_temp),
    url(r'^timebytempbyresponse/plus/(\d{1,2})/add/(\d{1,2})$', hours_ahead_by_temp_by_render_to_response),
    url(r'^hello/$', hello),
    url(r'^sample', sample),
    url(r'^carol', carol),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root':  os.path.join(BASE_DIR, r'resources/').replace('\\','/'),'show_indexes':True}),
)
