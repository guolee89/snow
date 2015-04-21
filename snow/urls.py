from django.conf.urls import patterns, include, url

import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'snow.views.home', name='home'),
    url(r'xadmin/', include(xadmin.site.urls)),

)
